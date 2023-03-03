"""vectors.py unit test"""
import ngspicehlp as ng


def test_vectors_one_signal_list():
    """vector with one signal initialized as a list"""
    sig1 = "signal_1"
    vector_single = ng.Vectors([sig1])
    assert str(vector_single) == sig1
