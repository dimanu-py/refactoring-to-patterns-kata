from mypyc.irbuild.builder import overload


class ProductPackage:

    _tv_channels: list[str]
    _telephone_number: int
    _internet_label: str

    @overload
    def __init__(self, internet_label: str) -> None:
        ...

    @overload
    def __init__(self, internet_label: str, telephone_number: int | None) -> None:
        ...

    @overload
    def __init__(self, internet_label: str, telephone_number: int | None, tv_channels: list[str] | None) -> None:
        ...

    def __init__(self, internet_label: str, telephone_number: int | None = None, tv_channels: list[str] | None = None) -> None:
        self._internet_label = internet_label
        self._telephone_number = telephone_number
        self._tv_channels = tv_channels

    def has_internet(self) -> bool:
        return self._internet_label is not None

    def has_phone_number(self) -> bool:
        return self._telephone_number is not None

    def has_tv_channels(self) -> bool:
        return self._tv_channels is not None
