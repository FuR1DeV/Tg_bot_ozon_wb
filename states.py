from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminStatesOzon(StatesGroup):
    title: State = State()
    type_product: State = State()
    article_product: State = State()
    price: State = State()
    link: State = State()
    link_utm: State = State()
    photo: State = State()


class AdminStatesWb(StatesGroup):
    title: State = State()
    type_product: State = State()
    article_seller: State = State()
    article_product: State = State()
    price_spp: State = State()
    link: State = State()
    photo: State = State()
