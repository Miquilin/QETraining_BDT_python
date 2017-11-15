from behave import given, when, then

# @given(u'I have $100 in my account')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I have $100 in my account')
#
# @given(u'I have $250 in my account')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I have $100 in my account')

@given(u'We have behave installed')
def step_impl(context):
    print("behave was installed")


@when(u'We implement a test')
def step_impl(context):
    print("doing an action")


@then(u'Behave will test it for us!')
def step_impl(context):
    print("A validation should be added")


@given(u'I have ${amount:d} in my account')
def step_impl(context, amount):
    print("The amount is:", amount)
