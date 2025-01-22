class User:
    def __init__(self, username, active_plan, duration_plan, referral_code):
        self.username = username
        self.active_plan = active_plan
        self.duration_plan = duration_plan
        self.referral_code = referral_code

    def get_user_plan(self):
        print(f'Plan yang kamu miliki: {self.active_plan}')
        print(f'Durasi plan: {self.duration_plan} bulan')
        plan_now_index = plan_type.index(self.active_plan)
        print('Benefit plan: ')
        for key, plan in enumerate(plan_benefit[plan_now_index]):
            print(f'{key+1}. {plan_services[key]}: {plan}')

    def get_plan(self, num):
        print(f'=> {plan_type[num]}:\n')
        for key, plan in enumerate(plan_benefit[num]):
            print(f'{key+1}. {plan_services[key]}: {plan}')
        print('=====================\n')

    def get_price(self, num):
        return plan_benefit[num][7]
    
    def get_all_referral_code(self, users):
        return [self.referral_code for i in users]

    def buy_plan(self, users):
        print(f'Your plan type: {self.active_plan}')
        print('Available plan to purchase: ')
        plan_now_index = plan_type.index(self.active_plan)

        for key in range(3):
            if plan_now_index == 2:
                print("There are no other plan to purchase")
                return
            elif plan_now_index < key:
                self.get_plan(key)
        
        plan_choosed = input('Pilih jenis plan yang ingin dibeli (cth: Standard): ')
        price = self.get_price(plan_type.index(plan_choosed))
        if self.duration_plan > 12:
            price -= 0.05*price
            print(f'Total yang harus dibayar: {price}')
        elif self.referral_code in self.get_all_referral_code(users):
            price -= 0.04*price
            print(f'Total yang harus dibayar: {price}')
        else:
            print(f'Total yang harus dibayar: {price}')

        self.active_plan = plan_choosed
        self.duration_plan = 0
        print('Plan berhasil dibeli')
        self.get_user_plan()

plan_type = ['Basic', 'Standard', 'Premium']
plan_benefit = [['yes', 'yes', 'yes', 'no', 'no', '1', '3rd party movie only', 120000],
                [ 'yes', 'yes', 'yes', 'yes', 'no', '2', 'basic plan content + sports (F1, Football, Basketball)', 160000],
                ['yes', 'yes', 'yes', 'yes', 'yes', '4', 'basic plan + standard plan + NeoFlix original series or movie', 200000]]
plan_services = ['can_stream', 'can_download', 'has_sd', 'has_hd', 'has_uhd', 'num_of_devices', 'content', 'price']