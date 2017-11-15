@given(u'I have loaded the registry form')
def step_impl(context):
    print("form is loaded")

@when(u'User set {zipCode:d} value on Zip Code field')
def step_impl(context, zipCode):
    print(zipCode)

@when(u'User set {country:w} value on Country code field')
def step_impl(context, country):
    print(country)


@when(u'User set {numHabitats:d} on Number Habitats field')
def step_impl(context, numHabitats):
    print(numHabitats)


@when(u'User press on Save button')
def step_impl(context):
    print("User press on save button")

@then(u'User is saved on BD')
def step_impl(context):
    print("Data is saved in database")