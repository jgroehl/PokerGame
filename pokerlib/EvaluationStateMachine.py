from pokerlib import Evalutaor


class StateDevice(object):
    def __init__(self):
        self.state = None
        self.used_card_indices = []

    def on_event(self, event, index):
        if self.state is None:
            raise BrokenPipeError("self.state not defined")
        self.state = self.state.on_event(event, index, self)

    def add_card_index(self, card_index):
        if card_index not in self.used_card_indices:
            self.used_card_indices.append(card_index)


class FlushStateDevice(StateDevice):

    def __init__(self):
        super(FlushStateDevice, self).__init__()
        self.state = InitSuitState()


class StraightStateDevice(StateDevice):

    def __init__(self):
        super(StraightStateDevice, self).__init__()
        self.state = InitStraightState()


class CardValueStateDevice(StateDevice):

    def __init__(self):
        super(CardValueStateDevice, self).__init__()
        self.state = ValueInitState()


class State(object):

    #def __init__(self):
    #   print("Now in state", self.__str__())

    def on_event(self, event, index, device):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

    def evaluate(self):
        return Evalutaor.HIGH_CARD


class InitSuitState(State):
    def on_event(self, event, index, device):
        if event == 0:
            return TwoSuitState()
        else:
            return InitSuitState()


class TwoSuitState(State):
    def on_event(self, event, index, device):
        if event == 0:
            return ThreeSuitState()
        else:
            return InitSuitState()


class ThreeSuitState(State):
    def on_event(self, event, index, device):
        if event == 0:
            return FourSuitState()
        else:
            return InitSuitState()


class FourSuitState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index-3, index+2):
                device.add_card_index(i)
            return FlushState()
        else:
            return InitSuitState()


class FlushState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index-3, index+2):
                device.add_card_index(i)
        return FlushState()

    def evaluate(self):
        return Evalutaor.FLUSH


class InitStraightState(State):
    def on_event(self, event, index, device):
        if event == 1:
            device.add_card_index(index)
            device.add_card_index(index+1)
            return TwoStraightState()
        else:
            return InitStraightState()


class TwoStraightState(State):
    def on_event(self, event, index, device):
        if event == 1:
            device.add_card_index(index + 1)
            return ThreeStraightState()
        elif event == 0:
            return TwoStraightState()
        else:
            return InitStraightState()


class ThreeStraightState(State):
    def on_event(self, event, index, device):
        if event == 1:
            device.add_card_index(index + 1)
            return FourStraightState()
        elif event == 0:
            return ThreeStraightState()
        else:
            return InitStraightState()


class FourStraightState(State):
    def on_event(self, event, index, device):
        if event == 1:
            device.add_card_index(index + 1)
            return StraightState()
        elif event == 0:
            return FourStraightState()
        else:
            return InitStraightState()


class StraightState(State):
    def on_event(self, event, index, device):
        if event == 1:
            device.add_card_index(index + 1)
        return StraightState()

    def evaluate(self):
        return Evalutaor.STRAIGHT


class ValueInitState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index+2):
                device.add_card_index(i)
            return FirstPairState()
        else:
            return ValueInitState()


class FirstPairState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return ThreeOfAKindState()
        else:
            return PairState()

    def evaluate(self):
        return Evalutaor.PAIR


class PairState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FirstTwoPairState()
        else:
            return PairState()

    def evaluate(self):
        return Evalutaor.PAIR


class FirstTwoPairState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FirstFullHouseState()
        else:
            return TwoPairState()

    def evaluate(self):
        return Evalutaor.TWO_PAIR


class TwoPairState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FirstTwoPairState()
        else:
            return TwoPairState()

    def evaluate(self):
        return Evalutaor.TWO_PAIR


class FirstFullHouseState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FourOfAKindState()
        else:
            return FullHouseState()

    def evaluate(self):
        return Evalutaor.FULL_HOUSE


class FullHouseState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
        return FullHouseState()

    def evaluate(self):
        return Evalutaor.FULL_HOUSE


class FullHousePairState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FirstFullHouseState()
        return FullHouseState()

    def evaluate(self):
        return Evalutaor.FULL_HOUSE


class ThreeOfAKindState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FourOfAKindState()
        else:
            return ThreeOfAKindFinishedState()

    def evaluate(self):
        return Evalutaor.THREE_OF_A_KIND


class FourOfAKindState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
        return FourOfAKindState()

    def evaluate(self):
        return Evalutaor.FOUR_OF_A_KIND


class ThreeOfAKindFinishedState(State):
    def on_event(self, event, index, device):
        if event == 0:
            for i in range(index, index + 2):
                device.add_card_index(i)
            return FullHousePairState()
        else:
            return ThreeOfAKindFinishedState()

    def evaluate(self):
        return Evalutaor.THREE_OF_A_KIND
