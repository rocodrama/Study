import torch

is_cuda_available = torch.cuda.is_available()
print(f"CUDA 사용 가능 여부: {is_cuda_available}")

if is_cuda_available:
    gpu_count = torch.cuda.device_count()
    print(f"사용 가능한 GPU 개수: {gpu_count}개")

    for i in range(gpu_count):
        gpu_name = torch.cuda.get_device_name(i)
        print(f"{i}번 GPU 이름: {gpu_name}")

        device = torch.device(f'cuda:{i}' if is_cuda_available else 'cpu')
        print(f"설정된 장치: {device}")
else: 
    device = torch.device('cpu')
    print('CUDA를 사용할 수 없어 CPU로 설정.')