from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminStatesOzon(StatesGroup):
    title: State = State()
    type_product: State = State()
    article_product: State = State()
    price: State = State()
    link_utm: State = State()
    photo_ozon_1: State = State()
    photo_ozon_2: State = State()
    photo_ozon_3: State = State()
    photo_finish: State = State()


class AdminStatesWb(StatesGroup):
    title: State = State()
    type_product: State = State()
    article_seller: State = State()
    article_product: State = State()
    price_spp: State = State()
    link: State = State()
    photo_wb_1: State = State()
    photo_wb_2: State = State()
    photo_wb_3: State = State()
    photo_finish: State = State()


class AdminChangeOzon(StatesGroup):
    enter_id: State = State()
    title: State = State()
    type_product: State = State()
    article_product: State = State()
    price: State = State()
    link_utm: State = State()


class AdminChangeWb(StatesGroup):
    enter_id: State = State()
    title: State = State()
    type_product: State = State()
    article_seller: State = State()
    article_product: State = State()
    price_spp: State = State()
    link: State = State()


class UserChangeOzon(StatesGroup):
    enter_id: State = State()


class UserChangeWb(StatesGroup):
    enter_id: State = State()
