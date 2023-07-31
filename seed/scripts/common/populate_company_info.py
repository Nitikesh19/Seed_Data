
from core.models.common.bank.details import BankDetailsModel
from core.models.common.address.shipping import ShippingAddressModel
from core.models.common.address.billing import BillingAddressModel


def populate_company_info(data, company):

    company_ship_address = ShippingAddressModel(
        attention=data['shipping_attention'], line1=data['shipping_line1'], line2=data['shipping_line2'],
        phone=data['shipping_contact_number'], zip=data['shipping_zip'], city=data['shipping_city'],
        state=data['shipping_state'], country=data['shipping_country']
    )
    company_ship_address.save()

    company_bill_address = BillingAddressModel(
        attention=data['billing_attention'], line1=data['billing_line1'], line2=data['billing_line2'],
        phone=data['billing_contact_number'], zip=data['billing_zip'], city=data['billing_city'],
        state=data['billing_state'], country=data['billing_country']
    )
    company_bill_address.save()

    bank_account_details = BankDetailsModel(
        bank_name=data['bank_account_name'], account_number=data['bank_account_number'],
        ifsc_code=data['bank_ifsc_code'], account_type=data['bank_account_type'],
        branch_name=data['bank_branch_name']
    )
    bank_account_details.save()

    company.name = data['company_name']
    company.display_name = data['display_name']
    company.email = data['company_email']
    company.phone = data['company_phone']
    company.currency = data['currency']
    company.website = data['website']
    company.country = data['country']
    company.shipping_address = company_ship_address
    company.billing_address = company_bill_address
    company.bank_details = bank_account_details

    return company

