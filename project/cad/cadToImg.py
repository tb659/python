import os
from pathlib import Path
import subprocess
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from matplotlib import font_manager

# -----------------------------
# 配置路径
# -----------------------------
input_folder = Path("input")      # DWG/DXF 输入目录
output_folder = Path("output")    # PNG 输出目录
temp_folder = Path("temp_dxf")    # 临时 DXF 存放目录
output_folder.mkdir(exist_ok=True)
temp_folder.mkdir(exist_ok=True)

# 中文字体路径（请根据系统修改）
CHINESE_FONT_PATH = r"C:\Windows\Fonts\SimHei.ttf"
myfont = font_manager.FontProperties(fname=CHINESE_FONT_PATH)

# ODAFileConverter 路径（确保已安装并加入环境变量）
ODA_PATH = "D:\Program Files\ODA\ODAFileConverter\ODAFileConverter.exe"  # 或者完整路径

# -----------------------------
# DWG → DXF 转换
# -----------------------------
def dwg_to_dxf(dwg_path: Path) -> Path:
    dxf_path = temp_folder / f"{dwg_path.stem}.dxf"
    try:
        # ODAFileConverter 参数说明：
        # 输入目录, 输出目录, DWG 文件名, 输出版本, DXF, 0=convert all, 1=overwrite, /shx_as_text 强制 SHX 转 TrueType
        cmd = f'"{ODA_PATH}" "{dwg_path.parent}" "{temp_folder}" "{dwg_path.name}" "ACAD2018" "DXF" 0 1 /shx_as_text'
        print(f"🛠️ 执行转换: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ 转换失败: {dwg_path.name}\n{result.stderr}")
            return None
        if not dxf_path.exists():
            print(f"❌ DXF 文件未生成: {dxf_path}")
            return None
        return dxf_path
    except Exception as e:
        print(f"❌ DWG 转 DXF 出错: {dwg_path.name} - {e}")
        return None

# -----------------------------
# 自定义 Matplotlib Backend 支持中文
# -----------------------------
class MatplotlibBackendCN(MatplotlibBackend):
    def draw_text(self, text, transform, font=None, cap_height=1.0,
                  valign='baseline', halign='left', rotation=0, **kwargs):
        if font is None:
            font = {"fontproperties": myfont, "size": 12}
        super().draw_text(text, transform, font=font, cap_height=cap_height,
                          valign=valign, halign=halign, rotation=rotation, **kwargs)

# -----------------------------
# 主循环
# -----------------------------
for cad_file in input_folder.glob("*.*"):
    if cad_file.suffix.lower() not in [".dwg", ".dxf"]:
        continue

    try:
        print(f"\n🎨 正在处理: {cad_file.name}")

        # 如果是 DWG，则转换为 DXF
        if cad_file.suffix.lower() == ".dwg":
            dxf_file = dwg_to_dxf(cad_file)
            if not dxf_file:
                print(f"❌ 跳过: {cad_file.name} 转换失败")
                continue
        else:
            dxf_file = cad_file

        # 读取 DXF
        doc = ezdxf.readfile(dxf_file)
        msp = doc.modelspace()
        ctx = RenderContext(doc)

        # 创建 Matplotlib 图像窗口
        fig = plt.figure(figsize=(12, 12), dpi=600)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()
        ax.set_facecolor("white")

        # 使用自定义中文 Backend 绘制
        backend = MatplotlibBackendCN(ax)
        frontend = Frontend(ctx, backend)
        frontend.draw_layout(msp, finalize=True)

        # 保存 PNG
        out_path = output_folder / f"{cad_file.stem}.png"
        plt.savefig(out_path, dpi=600, bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        print(f"✅ 导出成功: {out_path}")

    except Exception as e:
        print(f"❌ 转换失败: {cad_file.name} - {e}")

print("\n🚀 全部文件已转换完成！")
