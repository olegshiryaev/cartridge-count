from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render
from .models import Device, Cartridge, Mount
from .filters import MountFilter, CartridgeFilter, DeviceFilter
from .forms import MountForm, DeviceForm, DeviceUpdateForm
from django.shortcuts import redirect
from django.core.paginator import Paginator


@login_required()
def show_all_device(request):  # Список всех устройств
    devices = Device.objects.all()
    
    deviceFilter = DeviceFilter(request.GET, queryset=devices)
    devices = deviceFilter.qs

    paginated_filtered_devices = Paginator(deviceFilter.qs, 10)
    page_number = request.GET.get('page')
    device_page_obj = paginated_filtered_devices.get_page(page_number)

    context = {'device_page_obj': device_page_obj,
                'devices': devices,
               'deviceFilter': deviceFilter}

    return render(request, 'ink/devices.html', context)


@login_required()
def show_one_device(request, pk):  # Ифнормация о выбранном устройстве
    device = Device.objects.get(unit_id=pk)

    mounts = device.mount_set.all()
    mounts_count = mounts.count()

    myFilter = MountFilter(request.GET, queryset=mounts)
    mounts = myFilter.qs

    return render(request, 'ink/device.html', {
        'device': device, 'mounts': mounts, 'mounts_count': mounts_count, 'myFilter': myFilter
    })


@login_required()
def device_create(request):  # Форма создания нового устройства
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DeviceForm()
    return render(request,
                  'ink/device_create.html',
                  {
                      'form': form
                  })


def device_update(request, pk):  # Форма редактирования устройства
    device = Device.objects.get(unit_id=pk)
    form = DeviceUpdateForm(instance=device)

    previous_page = request.GET.get(
        'next') if request.GET.get('next') is not None else ''
    if request.method == 'POST':
        form = DeviceUpdateForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            redirect(previous_page) if previous_page != '' else redirect('home')

    context = {'form': form}
    return render(request, 'ink/device_update.html', context)


@login_required()
def cartridgeList(request):  # Список остатков картриджей
    cartridges = Cartridge.objects.all()

    cartridgeFilter = CartridgeFilter(request.GET, queryset=cartridges)
    cartridges = cartridgeFilter.qs

    paginated_filtered_cartridges = Paginator(cartridgeFilter.qs, 10)
    page_number = request.GET.get('page')
    cartridge_page_obj = paginated_filtered_cartridges.get_page(page_number)


    context = {'cartridge_page_obj': cartridge_page_obj,
               'cartridges': cartridges,
               'cartridgeFilter': cartridgeFilter}

    return render(request, 'ink/cartridges.html', context)


@login_required()
def createMount(request, pk):  # Форма установки картриджа на устройство
    device = Device.objects.get(unit_id=pk)
    MountFormSet = inlineformset_factory(Device, Mount, fields=(
        'cartridge', 'quantity', 'query'), extra=1, can_delete=False)
    formset = MountFormSet(queryset=Mount.objects.none(), instance=device)
    previous_page = request.GET.get(
        'next') if request.GET.get('next') is not None else ''
    if request.method == 'POST':
        formset = MountFormSet(request.POST, instance=device)
        if formset.is_valid():
            formset.save()
            return redirect(previous_page) if previous_page != '' else redirect('home')

    else:
        formset = MountFormSet()

    return render(request, 'ink/mount_form.html', {'formset': formset})


@login_required()
def updateMount(request, pk):  # Форма редактирования установки картриджа
    mount = Mount.objects.get(id=pk)
    form = MountForm(instance=mount)
    previous_page = request.GET.get(
        'next') if request.GET.get('next') is not None else ''
    if request.method == 'POST':
        form = MountForm(request.POST, instance=mount)
        if form.is_valid():
            form.save()
            return redirect(previous_page) if previous_page != '' else redirect('home')

    context = {'form': form}
    return render(request, 'ink/update_mount_form.html', context)


@login_required()
def deleteMount(request, pk):  # Удаление записи с установкой картриджа
    mount = Mount.objects.get(id=pk)
    previous_page = request.GET.get(
        'next') if request.GET.get('next') is not None else ''
    if request.method == "POST":
        mount.delete()
        return redirect(previous_page) if previous_page != '' else redirect('home')

    context = {'item': mount}
    return render(request, 'ink/delete.html', context)
