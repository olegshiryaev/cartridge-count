from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render
from .models import Device, Cartridge, Mount, Storage
from .filters import MountFilter, CartridgeFilter, DeviceFilter
from .forms import MountForm, DeviceForm, DeviceUpdateForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
import socket
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_control


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def show_all_device(request):  # Список всех устройств
    device_list = Device.objects.all()
    context = {'devices': device_list}

    return render(request, 'ink/devices.html', context)


@login_required()
def cartridgeList(request):  # Список остатков картриджей
    cartridges = Cartridge.objects.all()
    context = {'cartridges': cartridges}

    return render(request, 'ink/cartridges.html', context)


# Function to ADD Device
def device_create(request):
    if request.method=="POST":
        if request.POST.get('unit_id') \
            and request.POST.get('type') \
            and request.POST.get('model') \
            or request.POST.get('location'):
            device = Device()
            device.unit_id = request.POST.get('unit_id')
            device.type = request.POST.get('type')
            device.model = request.POST.get('model')
            device.location = request.POST.get('location')
            device.save()
            messages.success(request, "Устройство успешно добавлено!")
            return HttpResponseRedirect("/")
    else:
            return render(request, 'device_create.html')

# Function to Edit Employee
def device_update(request):
    if request.method == "POST":
        device = Device.objects.get(unit_id = request.POST.get('unit_id'))
        if device != None:
            device.unit_id = request.POST.get('unit_id')
            device.type = request.POST.get('type')
            device.model = request.POST.get('model')
            device.location = request.POST.get('location')
            device.save()
            messages.success(request, "Employee updated successfully !")
            return HttpResponseRedirect("/")

@login_required()
def createMount(request, pk):  # Форма установки картриджа на устройство
    device = Device.objects.get(unit_id=pk)
    MountFormSet = inlineformset_factory(Device, Mount, fields=[
        'storage', 'cartridge', 'quantity', 'query', 'initiator', 'counter', 'note'], extra=1, can_delete=False)
    mount_formset = MountFormSet(queryset=Mount.objects.filter(), instance=device)
    previous_page = request.GET.get(
        'next') if request.GET.get('next') is not None else ''
    if request.method == 'POST':
        mount_formset = MountFormSet(request.POST, instance=device)
        if mount_formset.is_valid():
            new_instances = mount_formset.save(commit=False)
            for new_instance in new_instances:

                new_instance.cartridge = Mount.objects.filter(cartridge)
                quantity = request.POST.get("quantity")
                new_instance.cartridge.amount -= int(quantity)
                new_instance.creator = request.user
                new_instance.save()
            messages.success(request, "Картридж успешно установлен")
            return redirect(previous_page) if previous_page != '' else redirect('home')

    else:
        mount_formset = MountFormSet()

    context = {'mount_formset': mount_formset}
    return render(request, 'ink/mount_form.html', context)

@login_required()
def show_one_device(request, pk):  # Ифнормация о выбранном устройстве
    device = Device.objects.get(unit_id=pk)

    mounts = device.mount_set.order_by('-created_at', '-query')
    mounts_count = mounts.count()

    myFilter = MountFilter(request.GET, queryset=mounts)
    mounts = myFilter.qs
    
    # if len(device.unit_id) <= 3:
    #     h_name = ('pszar00' + str(device.unit_id))
    # else:
    #     h_name = ('pszar0' + str(device.unit_id))
    # try:
    #     ip_address = socket.gethostbyname('h_name')
    #     print(ip_address)
    # except socket.gaierror:
    #     print(f'Устройство не сетевое')

    return render(request, 'ink/device.html', {
        'device': device, 'mounts': mounts, 'mounts_count': mounts_count, 'myFilter': myFilter
    })

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
            messages.success(request, "Установка картриджа отредактирована")
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
        messages.success(request, "Установка картриджа успешно удалена")
        return redirect(previous_page) if previous_page != '' else redirect('device', pk=mount.device.unit_id)
    context = {'mount': mount}
    return render(request, 'ink/delete.html', context)