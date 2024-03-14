from django.shortcuts import render, redirect
from django.views import View

from flower_app.forms import ConsultationRequestForm
from flower_app.models import ConsultationRequest, Bouquet


def index(request):

    consultation_request_form = ConsultationRequestForm(request.GET)
    bouquets = Bouquet.objects.all()
    bouquets_list = []
    for x in bouquets:
        image_absolute_path = request.build_absolute_uri(x.image.url)
        bouquet = {
            "bouquet_name": x.name,
            "bouquet_price": float(x.price),
            "bouquet_image": image_absolute_path,
        }
        bouquets_list.append(bouquet)
    return render(
        request,
        "FlowerApp/index.html",
        {
            "bouquets": bouquets_list[:3],
            "consultation_request_form": consultation_request_form,
        },
    )


def order(request):
    return render(request, "FlowerApp/order.html")


def catalog(request):
    consultation_request_form = ConsultationRequestForm(request.GET)
    return render(
        request,
        "FlowerApp/catalog.html",
        {"consultation_request_form": consultation_request_form},
    )


class ConsultationRequestView(View):
    template_name = "FlowerApp/consultation.html"

    def get(self, request):
        consultation_request_form = ConsultationRequestForm(request.GET)
        return render(
            request,
            self.template_name,
            {"consultation_request_form": consultation_request_form},
        )

    def post(self, request):
        consultation_request_form = ConsultationRequestForm(request.POST)
        if consultation_request_form.is_valid():
            name = consultation_request_form.cleaned_data["name"]
            phone_number = consultation_request_form.cleaned_data["phone_number"]
            ConsultationRequest.objects.create(name=name, phone_number=phone_number)
            return redirect("index")
        return render(
            request,
            self.template_name,
            {"consultation_request_form": consultation_request_form},
        )
