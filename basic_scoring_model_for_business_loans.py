from colorama import Fore
from colorama import Style

current_revenue = 0
total_revenue_of_group = 0
total_ebitda_of_group = 0
total_financial_debt_of_group = 0
list_of_co_debtors = []
total_equity = 0
total_assets = 0
num_co_debtors = 0
co_debtors = ""

print(f'{Fore.GREEN}Hello! This is a scoring model for applying business loans!'
      f', please fill the following information!{Style.RESET_ALL}')

name_of_company = input(f'{Fore.BLUE}Name of the Company{Style.RESET_ALL} applying for loan: ')

while co_debtors.lower() != "yes" or co_debtors.lower() != "no":
    if co_debtors.lower() == "yes":
        num_co_debtors = int(input('Enter the number of co-debtors: '))
        for index in range(num_co_debtors):
            name_of_co_debtor = input(f'{Fore.BLUE}Name of Co-debtor{index + 1}{Style.RESET_ALL}: ')
            list_of_co_debtors.append(name_of_co_debtor)
        break
    elif co_debtors.lower() == "no":
        break
    co_debtors = input(f'Is there {Fore.BLUE}Co-debtors{Style.RESET_ALL}. Yes/No: ')

while True:
    try:
        loan_amount_applying = int(input(f'The {Fore.GREEN}Amount of loan (in kBGN){Style.RESET_ALL} wants to apply: '))
        break
    except:
        print("Loan amount must be an integer!")

if loan_amount_applying >= 2000:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} Amount must be under 2 000 000 BGN.')
    exit()

while True:
    try:
        stage_of_companies = int(input(f'The {Fore.GREEN}Risk stage status{Style.RESET_ALL} [1,2 or 3] of the Group: '))
        break
    except:
        print("Stage must be a digit!")

if stage_of_companies != 1:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} It is acceptable risk status "Stage 1" only.')
    exit()

if num_co_debtors == 0:
    while True:
        try:
            internal_best_rating_of_companies = int(input(f'The {Fore.GREEN}internal rating{Style.RESET_ALL} of '
                                                          f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL}: '))
            break
        except:
            print("Rating must be a digit!")
else:
    while True:
        try:
            internal_best_rating_of_companies = int(
                input(f'Enter {Fore.GREEN}The Best internal rating{Style.RESET_ALL} of '
                      f'{Fore.BLUE}{name_of_company} and Co-debtors{Style.RESET_ALL}: '))
            break
        except:
            print("Rating must be a digit!")

num_of_companies_in_group = 1 + num_co_debtors

if internal_best_rating_of_companies >= 6:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} Best rating is above 6 and it is unacceptable.')
    exit()

for index in range(num_of_companies_in_group):
    if index == 0:
        while True:
            try:
                current_revenue = int(input(f'{Fore.GREEN}Revenue{Style.RESET_ALL} of {Fore.BLUE} '
                                            f'{name_of_company}{Style.RESET_ALL} for last year (in k BGN): '))
                break
            except:
                print("Revenue must be an integer!")

        while True:
            try:
                # Earning before interest, tax, depreciation and amortization:
                ebitda = int(input(f'{Fore.GREEN}EBITDA{Style.RESET_ALL} of '
                                   f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} for last year (in k BGN): '))
                break
            except:
                print("EBITDA must be an integer!")

        while True:
            try:
                # Existing loans:
                financial_debt = int(input(f'The {Fore.GREEN}Total financial debt{Style.RESET_ALL} of '
                                           f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL}'
                                           f' for last year(in k BGN): '))
                break
            except:
                print("Total financial debt must be an integer!")

        while True:
            try:
                equity = int(input(f'{Fore.GREEN}Amount of EQUITY{Style.RESET_ALL} of '
                                   f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} '
                                   f'for last year(in k BGN): '))
                break
            except:
                print("EQUITY must be an integer!")

        while True:
            try:
                assets = int(input(f'{Fore.GREEN}Total Assets{Style.RESET_ALL} of '
                                   f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} '
                                   f'for last year(in k BGN): '))
                break
            except:
                print("Total Assets must be an integer!")

    else:
        while True:
            try:
                current_revenue = float(input(f'{Fore.GREEN}Revenue{Style.RESET_ALL} of '
                                              f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                                              f'for last year (in k BGN): '))
                break
            except:
                print("Revenue must be an integer!")

        while True:
            try:
                ebitda = float(
                    input(f'{Fore.GREEN}EBITDA{Style.RESET_ALL} of {Fore.BLUE}{list_of_co_debtors[index - 1]} '
                          f'{Style.RESET_ALL} for last year (in k BGN): '))
                break
            except:
                print("EBITDA must be an integer!")

        while True:
            try:
                financial_debt = float(input(f'{Fore.GREEN}Total financial debt{Style.RESET_ALL} of '
                                             f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                                             f'for last year (in k BGN): '))
                break
            except:
                print("Total financial debt must be an integer!")

        while True:
            try:
                equity = float(input(f'{Fore.GREEN}Amount of EQUITY{Style.RESET_ALL} of '
                                     f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                                     f'for last year (in k BGN): '))
                break
            except:
                print("EQUITY must be an integer!")

        while True:
            try:
                assets = float(input(f'{Fore.GREEN}Total Assets{Style.RESET_ALL} of '
                                     f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                                     f'for last year (in k BGN): '))
                break
            except:
                print("Total Assets must be an integer!")

    total_equity += equity
    total_assets += assets
    total_revenue_of_group += current_revenue
    total_ebitda_of_group += ebitda
    total_financial_debt_of_group += financial_debt

if total_equity <= 0 or total_equity / total_assets <= 0.3:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} EQUITY is low.')
    exit()
if loan_amount_applying > total_revenue_of_group * 0.4:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} Loan amount must be under 40% from Revenue.')
    exit()
else:
    if total_financial_debt_of_group / total_ebitda_of_group > 4:
        print(f'{Fore.RED}Not applicable.{Style.RESET_ALL}'
              f' Over leveraged company/group. DEBT/EBITDA must bu under 4.')
        exit()
    else:
        while True:
            try:
                collateral_valuation = int(input(f'{Fore.GREEN}Liquidity value of collateral: '))
                break
            except:
                print("Liquidity value of collateral must be an integer!")

        if collateral_valuation / loan_amount_applying > 0.8:
            if num_of_companies_in_group == 1:
                print(
                    f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} is {Fore.GREEN}approved{Style.RESET_ALL} '
                    f'for the amount of {int(loan_amount_applying)}k BGN')
                print(f'Summary of financial statement of the company:'
                      f'\nTotal EBITDA: {total_ebitda_of_group:.0f}k BGN'
                      f'\nTotal Financial debt: {total_financial_debt_of_group:.0f}k BGN'
                      f'\nTotal EQUITY: {total_equity:.0f}k BGN'
                      f'/{(total_equity / total_assets) * 100:.0f}%/')
            elif num_of_companies_in_group == 2:
                print(
                    f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} is {Fore.GREEN}approved{Style.RESET_ALL} for '
                    f'the amount of {int(loan_amount_applying)}k BGN with Co-debtor {list_of_co_debtors}.')
                print(f'Summary of financial statement of the group:'
                      f'\nTotal EBITDA: {total_ebitda_of_group:.0f}k BGN'
                      f'\nTotal Financial debt: {total_financial_debt_of_group:.0f}k BGN'
                      f'\nTotal EQUITY: {total_equity:.0f}k BGN'
                      f'/{(total_equity / total_assets) * 100:.0f}%/')
            elif num_of_companies_in_group > 2:
                print(
                    f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} is {Fore.GREEN}approved{Style.RESET_ALL} '
                    f'for the amount of {int(loan_amount_applying)}k BGN with Co-debtors: {list_of_co_debtors}.')
                print(f'Summary of financial statement of the group:'
                      f'\nTotal EBITDA: {total_ebitda_of_group:.0f}k BGN'
                      f'\nTotal Financial debt: {total_financial_debt_of_group:.0f}k BGN'
                      f'\nTotal EQUITY: {total_equity:.0f}k BGN'
                      f'/{(total_equity / total_assets) * 100:.0f}%/')
        else:
            print(f'{Fore.RED}Not enough collateral value.{Style.RESET_ALL} Minimum coverage must be 80%.')
            exit()
