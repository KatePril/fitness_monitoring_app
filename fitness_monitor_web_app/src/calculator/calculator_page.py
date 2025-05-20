from flask import render_template


class CalculatorPageProvider:

    @staticmethod
    def _calculate_steps(kilos_to_lose, target_days):
        calories_in_one_kilo = 7700
        calories_to_burn = kilos_to_lose * calories_in_one_kilo
        calories_per_day = calories_to_burn / target_days
        return int(calories_per_day / 0.04)

    @staticmethod
    def calculator_page_get(user_id=None):
        if user_id:
            return render_template('calculator_page.html', user_id=user_id)
        else:
            return render_template('calculator_page.html')

    @staticmethod
    def calculator_page_post(form, user_id=None):
        kilos = float(form.get("kilos"))
        days = int(form.get("days"))
        if kilos > 0 and days > 0:
            result = CalculatorPageProvider._calculate_steps(kilos, days)
            if user_id:
                return render_template('calculator_page.html', result=result, user_id=user_id)
            else:
                return render_template('calculator_page.html', result=result)
        else:
            return CalculatorPageProvider.calculator_page_get(user_id)