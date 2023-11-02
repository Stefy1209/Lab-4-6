import Domain
def test_create_cmp_number():
    rl_part = 32.67
    img_part = -0.246
    assert Domain.create_cmp_number(rl_part, img_part) == [rl_part, img_part]

def test_get_rl_part():
    rl_part = -23423.5
    img_part = 643.009
    cmp_number = Domain.create_cmp_number(rl_part, img_part)
    assert rl_part == Domain.get_rl_part(cmp_number)

def test_get_img_part():
    rl_part = -23423.5
    img_part = 643.009
    cmp_number = Domain.create_cmp_number(rl_part, img_part)
    assert img_part == Domain.get_img_part(cmp_number)

def test_set_rl_part():
    rl_part = -23423.5
    img_part = 643.009
    cmp_number = Domain.create_cmp_number(rl_part, img_part)
    rl_part = 34.097
    Domain.set_rl_part(cmp_number, rl_part)
    assert cmp_number == [rl_part, img_part]

def  test_set_img_part():
    rl_part = -23423.5
    img_part = 643.009
    cmp_number = Domain.create_cmp_number(rl_part, img_part)
    img_part = 36.4745
    Domain.set_img_part(cmp_number, img_part)
    assert cmp_number == [rl_part, img_part]

def test_cmp_abs():
    rl_part = 3
    img_part = -34.63
    cmp_number = Domain.create_cmp_number(rl_part, img_part)
    assert abs(Domain.cmp_abs(cmp_number) - 34.759) < 0.001
def test_cmp_number():
    test_create_cmp_number()
    test_get_rl_part()
    test_get_img_part()
    test_set_rl_part()
    test_set_img_part()
    test_cmp_abs()

def test_x_is_prime():
    assert Domain.x_is_prime(0) == False
    assert Domain.x_is_prime(1) == False
    assert Domain.x_is_prime(2) == True
    assert Domain.x_is_prime(121) == False
    assert Domain.x_is_prime(47) == True

def run_tests():
    test_cmp_number()
    test_x_is_prime()
