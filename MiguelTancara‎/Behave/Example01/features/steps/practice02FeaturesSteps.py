@given(u'The registry form loaded')
def step_impl(context):
    print("Registry form is loaded")

@when(u'User set {firstname:w} on FirstName field')
def step_impl(context, firstname):
    print(firstname)

@when(u'User set {lastname:w} on LastName field')
def step_impl(context, lastname):
    print(lastname)

@when(u'User set {myEmail:w} on Choose your username field')
def step_impl(context, myEmail):
    print(myEmail)

@when(u'User set {password:w} on Confirm your password field')
def step_impl(context, password):
    print(password)

@when(u'User seelect {month:w} option on Month combobox')
def step_impl(context, month):
    print(month)

@when(u'User set {day:d} on Day field')
def step_impl(context, day):
    print(day)

@when(u'User set {year:d} on Year field')
def step_impl(context, year):
    print(year)

@when(u'User select {gender:w} option on Gender combobox')
def step_impl(context, gender):
    print(gender)

@when(u'User set {email} on your current email addres field')
def step_impl(context, email):
    print(email)

@when(u'User press on Next button')
def step_impl(context):
    print("user press onNext button")

@then(u'All data intoduced in the form is validated')
def step_impl(context):
    print("Data introduced int he form is validated")

@then(u'The next screen is loaded')
def step_impl(context):
    print("Next screen is loaded")
