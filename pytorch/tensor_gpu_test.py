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

        # 텐서 이동 및 연산 확인
        cpu_tensor = torch.randn(3, 3)
        print(f"CPU 텐서 장치 확인: {cpu_tensor.device}")

        if device.type == 'cuda':
            gpu_tensor = cpu_tensor.to(device)
            print(f"GPU 텐서 장치 확인: {gpu_tensor.device}")

            result_gpu = gpu_tensor * 2 + 1
            result_cpu = result_gpu.to('cpu')
            print(result_cpu)
else: 
    device = torch.device('cpu')
    print('CUDA를 사용할 수 없어 CPU로 설정.')