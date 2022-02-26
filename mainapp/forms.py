from django import forms
from .models import Order

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, HTML


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('first_name'), css_class='col-lg-6'),
                Column(Field('surname'), css_class='col-lg-6'),
                HTML("""
                <div id="div_id_phone_number" class="form-group"> 
                    <label for="id_phone_number" class=" requiredField">Номер телефона<span class="asteriskField">*</span> </label> 
                    <div class=""> 
                        <input class='masked prefixed textinput textInput form-control' name="phone_number" maxlength="128" class="" required="" id="id_phone_number"
                        type="tel" data-pattern="+7 (***) ***-**-**" data-prefix="+7" placeholder="+7 (***) ***-**-**">
                    </div> 
                </div>
                """),
                InlineRadios('delivery_type'),
                Column(Field('address1'), css_class='col-lg-6 order-addresses'),
                Column(Field('address2'), css_class='col-lg-6 order-addresses'),
                css_class='row'
            ),
            HTML("""
            <input type="submit" value="Оставить заявку" class="btn btn-outline-dark form-group cart-submit">
            """),
        )

    class Meta:
        model = Order
        fields = ['first_name', 'surname', 'phone_number', 'delivery_type', 'address1', 'address2']