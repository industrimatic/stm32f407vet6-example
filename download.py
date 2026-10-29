import subprocess

project_name = "init"
linkers = ["cmsis-dap", "stlink", "jlink"]
mcus = ["stm32f1x", "stm32f4x"]

linker = linkers[0]
mcu = mcus[1]

subprocess.run(
    [
        "openocd",
        "-f",
        f"interface/{linker}.cfg",
        "-f",
        f"target/{mcu}.cfg",
        "-c",
        f"program ./build/Debug/{project_name}.elf verify reset exit",
    ]
)
