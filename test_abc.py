from test_func import main,second_main,third_main


def test_main(main):
    global element
    element,message_main=main
    assert message_main=='Working Fine'

def test_second_main(second_main(element)):
    element,message=second_main
    assert message=='Working Fine'