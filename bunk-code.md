``` html
<!-- form element for search results to try and log last viewed movement in a post request -->
<form method="POST" action="{% url 'search_results' result.slug %}">
    {% csrf_token %}
    <button class="dropdown-item" name="{{ result }}-select" value="{{ result.slug }}" type="submit">{{ result }}</button>
    </form>
```
views.py code for the above html - to go in search results
```py
def post(self, request, slug, *args, **kwargs):
        movement_from_library = get_object_or_404(Movement, slug=slug)
        # bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        last_viewed_movement_form = LastViewedMovementForm(data=request.POST)
        user_lm_record_query = UserNonAuthField.objects.filter(user_id=request.user.id)
        if user_lm_record_query == []:
            if last_viewed_movement_form.is_valid():
                lvm = last_viewed_movement_form.save(commit=False)
                lvm.user_id = request.user
                lvm.last_movement = movement_from_library
                lvm.save()
            return redirect('movement_detail', slug=slug)
        else:
            if last_viewed_movement_form.is_valid():
                user_lm_record = get_object_or_404(UserNonAuthField, user_id=request.user.id)
                user_lm_record.last_movement = movement_from_library
                user_lm_record.save()
            return redirect('movement_detail', slug=slug)

        query = request.GET.get('query').title()
        queries = query.split()
        results = Movement.objects.filter(movement_name__contains=query)
        return redirect('movement_detail', slug=slug)
```

the form created in forms.py
```py
class LastViewedMovementForm(forms.ModelForm):
    class Meta:
        model = UserNonAuthField
        fields = ('last_movement',)
```