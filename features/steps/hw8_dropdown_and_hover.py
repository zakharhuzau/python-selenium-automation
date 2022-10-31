from behave import when, then


@when('Select department by value {department}')
def select_department(context, department):
    context.app.main_page.select_department(department)


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_result_page.verify_department(department)


@when('Hovers over New Arrivals')
def hovers_over_new_arrivals(context):
    context.app.product_page.hover_over()

@then('Verify user can see the deals')
def verify_user_sees_deals(context):
    context.app.product_page.verify_user_sees_deals()