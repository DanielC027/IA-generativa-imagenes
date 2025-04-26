from PySide6.QtCore import QThread, Signal
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
import os


class ImageGenerationThread(QThread):
    device_used = Signal(str)  # Señal para enviar cpu o gpu
    image_generated = Signal(str)  # Señal para enviar la ruta de la imagen generada
    error_occurred = Signal(str)  # Señal para enviar errores

    def __init__(self, model_path, prompt, cfg, steps, height, width):
        super().__init__()
        self.model_path = model_path
        self.prompt = prompt
        self.cfg = cfg
        self.steps = steps
        self.height = height
        self.width = width

    def run(self):
        try:
            device_info = ""
            print(
                self.model_path,
                self.prompt,
                self.cfg,
                self.steps,
                self.height,
                self.width,
            )
            # GPU INFORMATION
            print("\n" + "_" * 30)
            print("Version torch: " + torch.__version__)
            print("Version cuda: ", end="")
            print(torch.version.cuda)  # Debe devolver una versión válida de CUDA
            # more info
            print(torch.cuda.is_available())
            print("\n" + "_" * 15)
            print(torch.cuda.device_count())

            device_info += (
                torch.cuda.get_device_name(0)
                if torch.cuda.is_available()
                else "No GPU found"
            )

            print(device_info)

            print("\n" + "_" * 30)

            # Cargar el modelo
            pipe = StableDiffusionPipeline.from_single_file(
                self.model_path,
                torch_dtype=(
                    torch.float16 if torch.cuda.is_available() else torch.float32
                ),
                use_safetensor=True,
            )

            # Usar GPU si está disponible
            device = "cuda" if torch.cuda.is_available() else "cpu"
            pipe = pipe.to(device)

            # Imprimir donde se cargo el modelo
            print(f"Modelo cargado en: {pipe.device}")
            device_info += f", '{pipe.device}'."

            # Cargar informacion de device
            self.device_used.emit(device_info)

            # Importar el scheduler adecuado
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(
                pipe.scheduler.config
            )

            # Generar la imagen
            image = pipe(
                self.prompt,
                num_inference_steps=self.steps,
                guidance_scale=self.cfg,
                height=self.height,
                width=self.width,
            ).images[0]

            # Guardar la imagen generada
            output_path = "image.png"
            image.save(output_path)

            # Emitir la señal con la ruta de la imagen generada
            self.image_generated.emit(output_path)

        except Exception as e:
            # Emitir el error si ocurre
            self.error_occurred.emit(str(e))
