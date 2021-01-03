import os
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseRedirect

source_dates = pd.read_csv("us-covid-dates.csv")

titles = {
    "ct": {
        "title": "CASE RATE REPORTED BY STATE | TOTAL",
        "subtitle": "TOTAL NUMBER OF CASES | AS OF THE DATE INDICATED"
    },
    "ck": {
        "title": "CASE RATE REPORTED BY STATE WITH NATIONWIDE AVERAGE | PER 100K",
        "subtitle": "NUMBER OF CASES PER 100 000 POPULATION | AS OF THE DATE INDICATED"
    },
    "dt": {
        "title": "DEATH RATE REPORTED BY STATE | TOTAL",
        "subtitle": "TOTAL NUMBER OF DEATHS | AS OF THE DATE INDICATED"
    },
    "dk": {
        "title": "DEATH RATE REPORTED BY STATE WITH NATIONWIDE AVERAGE | PER 100K",
        "subtitle": "NUMBER OF DEATHS PER 100 000 POPULATION | AS OF THE DATE INDICATE"
    }
}


def index(request):

    if request.method == "POST":
        log = open("log.txt", "w")
        log.write(request.POST["day"])
        log.close()
        log_p = open("log_p.txt", "w")
        log_p.write(request.POST["page"])
        log_p.close()
        return HttpResponseRedirect("/")

    log = open("log.txt", "r")
    day = log.read()
    log.close()
    wb = db = nd = nw = "active"
    if int(day) < 8:
        wb = "inactive"
    if int(day) == 1:
        db = "inactive"
    if int(day) == 343:
        nd = "inactive"
    if int(day) > 336:
        nw = "inactive"

    log_p = open("log_p.txt", "r")
    page = log_p.read()
    log_p.close()
    ct = ck = dt = dk = "inactive"
    err = ""
    if page == "ct":
        ct = "active"
    if page == "ck":
        ck = "active"
        err = "NO STATES WITH AT LEAST 1 CASE PER 100 000 POPULATION"
    if page == "dt":
        dt = "active"
        err = "NO STATES WITH REPORTED DEATHS"
    if page == "dk":
        dk = "active"
        err = "NO STATES WITH AT LEAST 1 DEATH PER 100 000 POPULATION"

    code = "0" * (3 - len(str(day))) + str(day)
    date_line = list(source_dates[(source_dates.id == int(day))]["date_line"])[0]


    context = {
        "day": day,
        "date_line": date_line,
        "test": code,
        "chart": {"name": page, "code": code, "title": titles[page]["title"], "subtitle": titles[page]["subtitle"]},
        "buttons": {
            "days": {"back": {"day": db, "week": wb}, "next": {"day": nd, "week": nw}},
            "cases": {"total": ct, "100k": ck}, "deaths": {"total": dt, "100k": dk}
        },
        "file": os.path.exists("polls/static/polls/test/" + page + "_" + code + ".svg"),
        "error": err
    }

    return render(request, "polls/index.html", context)


def about(request):
    return render(request, "polls/about.html")
