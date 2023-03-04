"""vectors.py unit test"""
import pytest
import ngspicehlp as ng


@pytest.mark.parametrize(
    "vec_input,expected_from_inputs",
    [
        (["sig1"], "sig1"),
        (["sig1", "sig2"], "sig1 sig2"),
        (["sig1", "sig1"], "sig1"),
        (["sig1 sig2", "sig3"], "sig1 sig2 sig3"),
        (["sig1", 5], "sig1 5"),
    ],
)
def test_vectors_input(vec_input, expected_from_inputs):
    """vector with one signal initialized as a list"""
    my_vector = ng.Vectors(vec_input)
    assert my_vector.__str__() == expected_from_inputs


def test_vector_union():
    """check union of vectors"""
    vec1 = ng.Vectors(["sig1", "sig2"])
    vec2 = ng.Vectors(["sig2", "sig3"])
    vec3 = ng.Vectors([vec1, vec2])

    assert vec3.__str__() == "sig1 sig2 sig3"


def test_vector_sort():
    vec1 = ng.Vectors(["sig2", "sig3", "sig1"])
    vec1.sort()

    assert vec1.__str__() == "sig1 sig2 sig3"


def test_vector_subtract():
    """check subtraction of vectro"""
    vec1 = ng.Vectors(["sig1", "sig2", "sig3"])
    vec2 = ng.Vectors(["sig2"])
    vec1.subtract(vec2)

    assert vec1.__str__() == "sig1 sig3"


def test_vector_list_out():
    """check when outputing a list of the vectors"""
    vec1 = ng.Vectors(["sig1", "sig3 sig2"])

    assert vec1.list_out() == ["sig1", "sig3", "sig2"]
