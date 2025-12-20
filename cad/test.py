import os
from pathlib import Path
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from matplotlib import font_manager

# 输入、输出路径
input_folder = Path("input")
output_folder = Path("output")
temp_folder = Path("temp_dxf")
output_folder.mkdir(exist_ok=True)
temp_folder.mkdir(exist_ok=True)

# 中文字体路径（请根据你的系统修改）
CHINESE_FONT_PATH = r"C:\Windows\Fonts\SimHei.ttf"
myfont = font_manager.FontProperties(fname=CHINESE_FONT_PATH)

# 🧠 转换 DWG → DXF 函数
def dwg_to_dxf(dwg_path: Path) -> Path:
    dxf_path = temp_folder / f"{dwg_path.stem}.dxf"
    try:
        # 如果系统安装了 ODAFileConverter 可以调用
        if os.system("ODAFileConverter") == 0:
            os.system(f'"ODAFileConverter" "{dwg_path.parent}" "{temp_folder}" {dwg_path.name} "ACAD2018" "DXF" 0 1')
        else:
            # ezdxf 尝试直接读取 DWG（可能失败）
            doc = ezdxf.readfile(dwg_path)
            doc.saveas(dxf_path)
        return dxf_path if dxf_path.exists() else None
    except Exception as e:
        print(f"❌ DWG 转换失败: {dwg_path.name} - {e}")
        return None

# 🔧 自定义 MatplotlibBackend 支持中文
class MatplotlibBackendCN(MatplotlibBackend):
    def draw_text(self, text, transform, font=None, cap_height=1.0,
                  valign='baseline', halign='left', rotation=0, **kwargs):
        # 强制使用中文字体
        if font is None:
            font = {"fontproperties": myfont, "size": 12}
        super().draw_text(text, transform, font=font, cap_height=cap_height,
                          valign=valign, halign=halign, rotation=rotation, **kwargs)

# 🎨 主循环
for cad_file in input_folder.glob("*.*"):
    if cad_file.suffix.lower() not in [".dwg", ".dxf"]:
        continue

    try:
        print(f"\n🎨 正在处理: {cad_file.name}")

        # DWG → DXF
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

        # 创建绘图窗口（高清）
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
