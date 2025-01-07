# CUDA install on windows

- Start the virtual environment
- Check the latest release in torch's website: https://pytorch.org/get-started/locally/
- Run the installation similar to this: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
- Test like this: 
```
import torch
torch.cuda.is_available()
```