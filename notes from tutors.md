Ed:
It's tricky for sure, but it's good to understand the core ideas about the Http response cycle works.
You have a path such as 'post_detail', which has a view attached to it, which handles WHAT happens when it's accessed.
The view by default will expect a GET request, like when you visit any page. It 'gets' the data you want to show and renders it in a template. However, you might have a form on your page (which is again rendered using the GET method, it 'gets' the form). When that form is submitted you want to SEND data and you use the POST method for that.
If your view receives a POST method, then you'll want to handle what happens differently. With the View view you need to override the post() method to tell it what should happen when it receives a POST request. After its done its work, you can redirect to a different path and view.
Hope that make some sense!

Normal use of Django will use Http responses, which means a reload of the page. If you wanted to do something without the page reloading you'd have to use a async request using javascript (e.g. using fetch or jQuery's ajax API). It's not as complex as it sounds, but quite a lot to take in if you're just getting used to Django.
You'd have a view which returned JsonResponse rather than Http, so when the script fetches a URL (can be get or post), it receives a response in Json format and can then make changes to the DOM using that returned json data. You will need to use javacsript for it though (or research htmx library, which lets you do all of it within your HTML).