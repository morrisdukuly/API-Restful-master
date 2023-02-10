from datetime import date
import pymysql
from app import app
from config import db
from Cash import Cash 
from check import Check  
from Credit import Credit 
from Item import Item
from Order import Order
from OrderDetail import OrderDetail
from OrderStatus import OrderStatus
from Payment import Payment 
#from WireTransfer import WireTransfer  

with app.app_context():
    db.create_all()
@app.route('/orderStatus', methods=['GET'])
def all_status():
    try:
        orderStatuss = OrderStatus.query.all()
        data = [{"id": orderStatus.id, "create": orderStatus.create,"shipping":orderStatus.shipping, "delivered" : orderStatus.delivered, "paid" : orderStatus.paid} for orderStatus in orderStatuss]
        resultat = jsonify({"statut_code": 200,"animals": data })
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur frère'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

if(__name__ == '__main__'):
    app.run()
