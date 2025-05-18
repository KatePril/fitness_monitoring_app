from flask import render_template
from fitness_monitor_web_app.src.calculator.calculate import calculate_steps


def calculator_page_get():
    return render_template('calculator_page.html')

def calculator_page_post(form):
    kilos = form.get("kilos")
    days = form.get("days")
    if kilos > 0 and days > 0:
        return render_template(
            'calculator_page.html',
            result=calculate_steps(kilos, days),
        )
    else:
        return calculator_page_get()