from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}


# Create your views here.
def monthly_challenge_by_number(reques, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month == 0:
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challege-url", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except Exception:
        return HttpResponseNotFound("This month is not supported!")


def index(request):
    index = """
<html>
<head>
    <title>Challenges</title>
        <ul>
            <li> <a href="">January</li>
            <li> <a href="">February</li>
            <li> <a href="">March</li>
            <li> <a href="">April</li>
            <li> <a href="">May</li>
            <li> <a href="">June</li>
            <li> <a href="">July</li>
            <li> <a href="">August</li>
            <li> <a href="">September</li>
            <li> <a href="">October</li>
            <li> <a href="">November</li>
        </ul>
</head>
</html>
"""
    return HttpResponse(index)
