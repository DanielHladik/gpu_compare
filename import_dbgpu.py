import dbgpu
from cards.models import GraphicsCard
from django.db import transaction

def get_int(val):
    try:
        return int(val)
    except (TypeError, ValueError):
        return None

def get_str(val):
    return str(val) if val is not None else ''

@transaction.atomic
def import_gpus():
    for row in dbgpu.gpus():
        GraphicsCard.objects.create(
            name=row.get('name', ''),
            manufacturer=row.get('vendor', '')[:10],
            memory_gb=get_int(row.get('memory')) or 0,
            memory_type=get_str(row.get('memory_type')),
            price=0,
            benchmark_index=0,
            cuda_cores=get_int(row.get('cuda')),
            tdp=get_int(row.get('tdp')),
            release_year=get_int(row.get('year')),
            bus=get_str(row.get('bus')),
            process=get_str(row.get('process')),
            base_clock=get_int(row.get('base_clock')),
            boost_clock=get_int(row.get('boost_clock')),
            directx=get_str(row.get('directx')),
            opengl=get_str(row.get('opengl')),
            opencl=get_str(row.get('opencl')),
            vulkan=get_str(row.get('vulkan')),
            shader_model=get_str(row.get('shader_model')),
            pixel_rate=get_str(row.get('pixel_rate')),
            texture_rate=get_str(row.get('texture_rate')),
            rops=get_int(row.get('rops')),
            tmus=get_int(row.get('tmus')),
        )
    print('Import hotov!')

if __name__ == '__main__':
    import_gpus()
