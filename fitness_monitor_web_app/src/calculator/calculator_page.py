from flask import render_template
from fitness_monitor_web_app.src.calculator.calculate import calculate_steps


def calculator_page_get(user_id=None):
    if user_id:
        return render_template('calculator_page.html', user_id=user_id)
    else:
        return render_template('calculator_page.html')

def calculator_page_post(form, user_id=None):
    kilos = float(form.get("kilos"))
    days = int(form.get("days"))
    if kilos > 0 and days > 0:
        result = calculate_steps(kilos, days)
        if user_id:
            return render_template('calculator_page.html', result=result, user_id=user_id)
        else:
            return render_template('calculator_page.html', result=result)
    else:
        return calculator_page_get(user_id)