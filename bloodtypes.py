"""
Blood group 0 individuals do not have A or B antigens. 
Therefore, a group 0 individual can receive blood only from a group 0 individual, but can donate blood to individual with types A, B, 0 or AB.

Blood group A individuals have the A antigen. 
Therefore, a group A individual can receive blood only from individuals of groups A or 0, and can donate blood to individuals with type A or AB.

Blood group B individuals have the B antigen. 
Therefore, a group B individual can receive blood only from individuals of groups B or 0, and can donate blood to individuals with type B or AB.

Blood group AB individuals have both A and B antigens. 
Therefore, an individual with type AB blood can receive blood from AB0, but cannot donate blood to any group other than AB.

Rh-D negative individuals do not have Rh-D antigen. 
Therefore, Rh-D negative can receive blood only from other Rh-D negative individuals.

Rh-D positive individuals have Rh-D antigen. 
Therefore, Rh-D positive individual can receive blood from both Rh-D negative or positive individuals.

Individuals with 0- are universal donors. 
Individuals with AB+ are universal recipients.

The rules described are general. In practice, there are over 340 different blood-group antigens.

Tasks Complete the function check_bt()
The function should check red blood cell compatibility between a donor and a recipient.

Return True for compatibility between the donor and the recipient, False otherwise.

If the input value is not a required type raise TypeError .

If the input value is not in the defined interval raise ValueError .
"""

def check_bt(donor, recipient):
    valid_blood_types = {'A', 'B', 'AB', 'O'}
    valid_rh_factors = {'+', '-'}

    if not isinstance(donor, str) or not isinstance(recipient, str):
        raise TypeError("Input Values must be strings!!")
    
    donor_blood_type, donor_rh_factor = donor[:-1], donor[:-1]
    recipient_blood_type, recipient_rh_factor = recipient[:-1], recipient[:-1]

    if donor_blood_type not in valid_blood_types or recipient_blood_type not in valid_blood_types:
        raise ValueError("Invalid Blood Type")
    
    if donor_rh_factor not in valid_rh_factors or recipient_rh_factor not in valid_rh_factors:
        raise ValueError("Invalid Rh factor")
    
    # check compatibility based on blood types and Rh factors
    if donor_blood_type == 'O' and donor_rh_factor == '-':
        return True
    
    if donor_blood_type == 'AB' and donor_rh_factor == '+':
        return True
    
    if donor_blood_type == '-' and donor_rh_factor == '-':
        return True
    
    if donor_rh_factor == '+' and recipient_rh_factor in {'+', '-'}:
        return True 

    # Check compatibility based on ABO blood groups
    if donor_blood_type == 'A' and recipient_blood_type in {'A', '0'}:
        return True

    if donor_blood_type == 'B' and recipient_blood_type in {'B', '0'}:
        return True

    if donor_blood_type == 'AB' and recipient_blood_type in {'A', 'B', 'AB', '0'}:
        return True

    if donor_blood_type == '0' and recipient_blood_type == '0':
        return True
    
    return False


donor = "O"
recipient = "O"
result = check_bt(donor, recipient)
print(result)