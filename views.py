class CustomDeviceBulkEditView(DeviceBulkEditView):
    form = forms.CustomDeviceBulkEditForm

    def post(self, request, **kwargs):

        model = self.queryset.model
        custom_form_fields = [
            "checkgroups"
        ]
        request_post_copy = request.POST.copy()

        if "_apply" in request.POST:
            form = self.form(model, request.POST)
            restrict_form_fields(form, request.user)

            if form.is_valid():
                for obj in self.queryset.filter(pk__in=form.cleaned_data["pk"]):
                    obj = self.alter_obj(obj, request, [], kwargs)
                    # Update related fields.
                    for field in custom_form_fields:
                        getattr(obj, field).set([form.cleaned_data[field]])
                        print(obj.checkgroups.all())

            for field in custom_form_fields:
                request_post_copy.pop(field)

            request.POST = request_post_copy

        return super().post(request, **kwargs)
