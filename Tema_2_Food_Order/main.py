condition_vip = False

delivery_free_limit = 500.00
order_cost = 400.00

delivery_wanted = input('do you want delivery ? (yes / no) ') == 'yes'

delivery_free_condition = delivery_free_limit <= order_cost

delivery_is_free = delivery_wanted and (
    condition_vip or delivery_free_condition)

delivery_wanted and print('free delivery is :', delivery_is_free)
