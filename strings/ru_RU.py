# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# English translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "₽"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} доступно"

# Copies of a product in cart
in_cart_format_string = "{quantity} в корзине"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Заказ #{id}"

# Order info string, shown to the admins
order_format_string = "От {user}\n" \
                      "Дата: {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "ИТОГ: <b>{value}</b>\n" \
                      "\n" \
                      "Комментарий пользователя: {notes}\n."

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Заказ {status_text}</b>\n" \
                           "{items}\n" \
                           "ИТОГ: <b>{value}</b>\n" \
                           "\n" \
                           "Комментарий: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Загружаю текущие покупки...\n" \
                       "Пожалуйста, немного подождите...</i>"

# Transactions page
transactions_page = "Страница <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Этот файл 📄 .csv содержит все заказы, выгруженные из базы данных бота.\n" \
              "Вы можете открыть этот файл, например, с помощью LibreOffice Calc" \

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Hello!\n" \
                           "Welcome to greed!\n" \
                           "What you see here is the 🅱️ <b>Beta</b> version of the software.\n" \
                           "It is fully usable, but it is possible that some bugs are still present.\n" \
                           "If you find any, you can collaborate with the developer to solve them, describing what" \
                           " happened at https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Что дальше?\n"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Вы 💼 <b>Admin</b> этого магазина!\n" \
                               "Что вы хотите сделать?\n" \
                               "\n" \
                               "<i>Чтобы выполнить действие, нажмите на нужную кнопку внизу клавиатуры.\n" \
                               "Если клавиатура не открыта, вы можете вызвать ее нажатимем на иконку с прямоугольниками" \
                               ", она находится на панели отправки сообщения.</i>"

# Conversation: select a payment method
conversation_payment_method = "How do you want to add funds to your wallet?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️  Какой продукт вы хотите редактировать?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Какой продукт вы хотите удалить?"

# Conversation: select a user to edit
conversation_admin_select_user = " Выберите пользователя для выполнения над ним действия."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Добавляйте заказы в корзину перемещаясь по экрану и нажимая на кнопку Добавить" \
                            ". Когда вы закончите, вернитесь обратно к этому сообщению" \
                            " и нажмите на кнопку Завершить.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Сейчас в вашей корзине:\n" \
                            "{product_list}" \
                            "Итого: <b>{total_cost}</b>\n" \
                            "\n" \

# Conversation: the user activated the live orders mode
conversation_live_orders_start = " Вы в режите <b>Live Orders</b>\n" \
                                 "Все новые заказы пользователей будут появляться здесь в реальном времени" \
                                 ". Вы можете завершить кнопкой ✅ Завершить" \
                                 " или ✴️ Вернуть деньги покупателю.\n" \
                                 "\n" \
                                 "<i>Нажмите на Остановить, чтобы выйти из этого режима </i>"

# Conversation: help menu has been opened
conversation_open_help_menu = " Какая помощь вам нужна?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = " Вы действительно хотите сделать этого пользователя администратором 💼 Admin?\n"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Вы в режиме покупателя 👤\n" \
                                   "Если вы хотите вернуться обратно в режим 💼 Администратора, введите /start."

# Notification: the conversation has expired
conversation_expired = "🕐  Я долго не получал от вас сообщений, поэтому завершил вашу сессию.\n" \
                       "Если хотите продолжить, начните с команды /start"

# User menu: order
menu_order = "🛒 Меню"

# User menu: order status
menu_order_status = "🛍 Мои заказы"

# User menu: add credit
menu_add_credit = "💵 Добавить деньжат"

# User menu: bot info
menu_bot_info = "ℹ️ Информация о боте"

# User menu: cash
menu_cash = "💵 Налик"

# User menu: credit card
menu_credit_card = "💳 Кредитная карта"

# Admin menu: products
menu_products = "📝️ Продукты"

# Admin menu: orders
menu_orders = "📦 Заказы"

# Menu: transactions
menu_transactions = "💳 Список платежей"

# Menu: edit credit
menu_edit_credit = "💰 Создать платеж"

# Admin menu: go to user mode
menu_user_mode = "👤 Перейти в режим пользователя"

# Admin menu: add product
menu_add_product = "✨ Новый продукт"

# Admin menu: delete product
menu_delete_product = "❌ Удалить продукт"

# Menu: cancel
menu_cancel = "🔙 Назад"

# Menu: skip
menu_skip = "⏭  Пропустить"

# Menu: done
menu_done = "✅️ Готово"

# Menu: pay invoice
menu_pay = "💳 Заплатить"

# Menu: complete
menu_complete = "✅ Готово"

# Menu: refund
menu_refund = "✴️  Возврат"

# Menu: stop
menu_stop = "🛑 Остановить"

# Menu: add to cart
menu_add_to_cart = "➕ Добавить"

# Menu: remove from cart
menu_remove_from_cart = "➖ Убрать"

# Menu: help menu
menu_help = "❓ Помощь и Поддержка"

# Menu: guide
menu_guide = "📖 Руководство"

# Menu: next page
menu_next = "▶️ Далее"

# Menu: previous page
menu_previous = "◀️ Назад"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Связаться с магазином"

# Menu: generate transactions .csv file
menu_csv = "📄.csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Редактировать администраторов"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = " В ожидании"

# Text: completed order
text_completed = " Готово"

# Text: refunded order
text_refunded = " Возврат"

# Add product: name?
ask_product_name = "Какое название будет у продукта?"

# Add product: description?
ask_product_description = "Какое описание будет у продукта?"

# Add product: price?
ask_product_price = "Какая будет цена?\n" \
                    "Напишите <code>X</code> если вы еще не готовы продавать этот продукт"

# Add product: image?
ask_product_image = "🖼 Какое изображение будет у продукта?\n" \
                    "\n" \
                    "<i>Просто отправьте мне фото, или не отправляйте, как хотите. В любой момент вы сможете отредактировать данный продукт </i>"

# Order product: notes?
ask_order_notes = " Напишите свой адрес и номер телефона\n" \
                  "\n" \

# Refund product: reason?
ask_refund_reason = " Напишите, почему вы хотите вернуть заказ?.\n"

# Edit credit: notes?
ask_transaction_notes = " Attach a note to this transaction.\n" \
                        "👤 It will be visible to the customer after crediting / debiting" \
                        " and to 💼 Admins in the transaction log."

# Edit credit: amount?
ask_credit = "How much do you want to change the customer's credit?\n" \
             "\n" \
             "<i>Send a message containing the amount.\n" \
             "Put a mark </i><code>+</code><i> if you want to add credit to the customer's account." \
             " or a sign </i><code>-</code><i>  you want to deduce it.</i>"

# Header for the edit admin message
admin_properties = "<b>Права администратора {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Изменять продукты"

# Edit admin: can receive orders?
prop_receive_orders = "Получать данные о заказах"

# Edit admin: can create transactions?
prop_create_transactions = "Получать данные о платежах"

# Edit admin: show on help message?
prop_display_on_help = "Будет отображаться в Поддержке"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Я загружаю ваше фото!\n" \
                    "Это может занять некоторое время...\n" \
                    "Я отвечу вам только после того, как загружу все фото."

# Edit product: current value
edit_current_value = "Текущая цена:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Нажмите Далее, чтобы пропустить изменение цены</i>"

# Payment: cash payment info
payment_done = "Оплачено"

payment_cancel = "Отмена"

payment_cash = "You can pay cash at the physical location of the store.\n" \
               "Pay at checkout, and provide the store admin with this id:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "How many funds do you want to add to your wallet?\n" \
                    "\n" \
                    "<i>Select an amount with the buttons below, or enter it manually with the keyboard" \
                    " normal.</i>"

# Payment: add funds invoice title
payment_invoice_title = "Adding funds"

# Payment: add funds invoice description
payment_invoice_description = "Paying this receipt will add {amount} to your wallet."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Перезагрузить"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Card supplement"

# Notification: order has been placed
notification_order_placed = "Размещен новый заказ:\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Ваш заказ собран!\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Your order has been refunded!\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  A new transaction has been applied to your wallet:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Refund reason:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = ' This bot uses <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' a framework by @Steffo for payments on Telegram released under the' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           ' Affero General Public License 3.0</a>.\n' \
           ' The source code of this version is available <i>here</i>.\n'

# Help: guide
help_msg = "Bot help is available at this address:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Help: contact shopkeeper
contact_shopkeeper = "В настоящее время, вам могут помочь: \n" \
                     "{shopkeepers}\n" \
                     "<i>Нажмите, чтобы связаться в Telegram.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Продукт успешно изменен/добавлен!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Продукт успешно удален!"

# Success: order has been created
success_order_created = "✅ Заказ обработан, пожалуйста, для оплаты следуйте по ссылке\n" \
                        "Подтвердите оплату кнопкой \"Оплачено\"\n" \
                        "\n" \
                        "{link}"

fail_order_payment = "Оплата за заказ {order_id} не прошла, если вы уверены, что оплатили заказ, обратитесь в службу " \
                     "поддержки "

fail_order_too_big = "Сумма вашего заказа превышает допустимое значение - {max}"

fail_order_too_small = "Слишком маленький заказ, минимальная сумма - {min} рублей"

# Success: order was marked as completed
success_order_completed = "✅ Вы отметили заказ #{order_id} как завершенный"

# Success: order was refunded successfully
success_order_refunded = "✴️ Order #{order_id} has been successfully refunded."

successfull_payment = "Оплата совершена, ожидайте курьера"

# Success: transaction was created successfully
success_transaction_created = "✅ The transaction was created successfully!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Бот работает только в приватных чатах."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ Сессия бота была прервана.\n" \
                           "Чтобы начать заново, отправьте боту команду /start."

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ the maximum of funds that can be added in a single transaction is " \
                                "{max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ The minimum of funds that can be added in a single transaction is " \
                                 "{min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ This payment has expired and has been canceled. If you still want to add funds, " \
                        "use the Add menu funds option. "

# Error: a product with that name already exists
error_duplicate_name = "⚠️ Такое имя продукта уже существует"

# Error: not enough credit to order
error_not_enough_credit = "⚠️ You do not have enough credit to place the order"

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Данный заказ, к сожалению, был отменен."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  У вас еще нет заказов."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  Выбранный пользователь не существует"

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Оо нет!<b>Ошибка</b> прервала работу чата\n" \
                               "Но не переживайте, сообщение об ошибке уже направлено разработчикам.\n" \
                               "Попробуйте начать заново командой /start."
