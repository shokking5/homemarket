# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# English translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "₽"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} available"

# Copies of a product in cart
in_cart_format_string = "{quantity} in cart"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Order #{id}"

# Order info string, shown to the admins
order_format_string = "of {user}\n" \
                      "Created on {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAL: <b>{value}</b>\n" \
                      "\n" \
                      "Customer notes: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Order {status_text}</b>\n" \
                           "{items}\n" \
                           "TOTAL: <b>{value}</b>\n" \
                           "\n" \
                           "Notes: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Loading current transactions...\n" \
                       "Please wait for a few seconds...</i>"

# Transactions page
transactions_page = "Page <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "A 📄 .csv file containing all transactions stored in the bot database was generated.\n" \
              "You can open this file with other programs, such as LibreOffice Calc, to process" \
              " data."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Hello!\n" \
                           "Welcome to greed!\n" \
                           "What you see here is the 🅱️ <b>Beta</b> version of the software.\n" \
                           "It is fully usable, but it is possible that some bugs are still present.\n" \
                           "If you find any, you can collaborate with the developer to solve them, describing what" \
                           " happened at https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "What would you like to do?\n" \
                              "💰 You have <b>{credit}</b> in your wallet.\n" \
                              "\n" \
                              "<i>Press a key on the keyboard at the bottom to select an operation.\n" \
                              "If the keyboard has not opened, you can open it by pressing the button with four small squares" \
                              " in the message bar.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "You are 💼 <b>Admin</b> of this store!\n" \
                               "What would you like to do?\n" \
                               "\n" \
                               "<i>to select an operation, Press a key on the keyboard at the bottom.\n" \
                               "If the keyboard has not opened, you can open it by pressing the button with four small squares" \
                               " in the message bar.</i>"

# Conversation: select a payment method
conversation_payment_method = "How do you want to add funds to your wallet?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ What product do you want to change?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ What product do you want to delete?"

# Conversation: select a user to edit
conversation_admin_select_user = " Select a user to perform the selected action on."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Add products to cart by scrolling up and pressing the Add button below" \
                            " the products you want to buy. When you're done, go back to this message and" \
                            " press the Done button.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Your cart contains these products:\n" \
                            "{product_list}" \
                            "Total: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>If you want to proceed, press the Done button below this message.\n" \
                            "To cancel, press the Cancel button.</i>"

# Conversation: the user activated the live orders mode
conversation_live_orders_start = "You are in <b>Live Orders</b> mode\n" \
                                 "All new orders placed by customers will appear in real time in this" \
                                 " chat, and you can mark them as ✅ Completed" \
                                 " or ✴️ Refund the credit to the customer.\n" \
                                 "\n" \
                                 "<i>Press the Stop button below this message to stop the" \
                                 " reception.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "What kind of assistance do you want to receive?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Are you sure you want to promote this user to 💼 Admin?\n" \
                                       "It is an irreversible action!"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " You are switching to 👤 Customer mode.\n" \
                                   "If you want to go back to the 💼 Admin menu, restart the conversation with /start."

# Notification: the conversation has expired
conversation_expired = "🕐  I haven't received any messages in a while, so I ended the conversation to save resources.\n" \
                       "If you want to start a new one, re-send the /start command."

# User menu: order
menu_order = "🛒 Orders"

# User menu: order status
menu_order_status = "🛍 My orders"

# User menu: add credit
menu_add_credit = "💵 Add funds"

# User menu: bot info
menu_bot_info = "ℹ️ Bot info"

# User menu: cash
menu_cash = "💵 Cash"

# User menu: credit card
menu_credit_card = "💳 Credit Card"

# Admin menu: products
menu_products = "📝️ Products"

# Admin menu: orders
menu_orders = "📦 Orders"

# Menu: transactions
menu_transactions = "💳 Transaction list"

# Menu: edit credit
menu_edit_credit = "💰 Create transaction"

# Admin menu: go to user mode
menu_user_mode = "👤 Press switch to customer mode"

# Admin menu: add product
menu_add_product = "✨ New product"

# Admin menu: delete product
menu_delete_product = "❌ Delete product"

# Menu: cancel
menu_cancel = "🔙 Cancel"

# Menu: skip
menu_skip = "⏭ Jump"

# Menu: done
menu_done = "✅️ Done"

# Menu: pay invoice
menu_pay = "💳 Pay"

# Menu: complete
menu_complete = "✅ Complete"

# Menu: refund
menu_refund = "✴️ Refund"

# Menu: stop
menu_stop = "🛑 Stop"

# Menu: add to cart
menu_add_to_cart = "➕ Add"

# Menu: remove from cart
menu_remove_from_cart = "➖ Remove"

# Menu: help menu
menu_help = "❓ Help / Support"

# Menu: guide
menu_guide = "📖 Manual"

# Menu: next page
menu_next = "▶️ Next"

# Menu: previous page
menu_previous = "◀️ Previous"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contact the store"

# Menu: generate transactions .csv file
menu_csv = "📄.csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Edit admins"

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
text_not_processed = "pending"

# Text: completed order
text_completed = "completed"

# Text: refunded order
text_refunded = "refunded"

# Add product: name?
ask_product_name = "What should be the product name?"

# Add product: description?
ask_product_description = "What should be the product description?"

# Add product: price?
ask_product_price = "What should be the product price?\n" \
                    "Write <code>X</code> if you want the product not for sale yet"

# Add product: image?
ask_product_image = "🖼 What image do you want the product to have?\n" \
                    "\n" \
                    "<i>Send the photo, or if you prefer to leave the product without any picture press the Skip " \
                    "button below.</i>"

# Order product: notes?
ask_order_notes = " Do you want to leave a note along with the order?\n" \
                  "💼 It will be visible to store admins.\n" \
                  "\n" \
                  "<i>Send a message with the note you want to leave, or press the Skip button below this" \
                  " message to leave nothing.</i>"

# Refund product: reason?
ask_refund_reason = " Attach a reason to this refund.\n" \
                    "👤  It will be visible to the customer."

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
admin_properties = "<b>Permissions {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Edit products"

# Edit admin: can receive orders?
prop_receive_orders = "Receive orders"

# Edit admin: can create transactions?
prop_create_transactions = "Manage transactions"

# Edit admin: show on help message?
prop_display_on_help = "Customer Support"

# Thread has started downloading an image and might be unresponsive
downloading_image = "I'm downloading your photo!\n" \
                    "It might take a while... Be patient!\n" \
                    "I will not be able to answer you while downloading."

# Edit product: current value
edit_current_value = "The current value is:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Press the jump button below this message to keep the same value.</i>"

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
payment_invoice_label = "Reload"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Card supplement"

# Notification: order has been placed
notification_order_placed = "A new order has been placed:\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Your order has been completed!\n" \
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
contact_shopkeeper = "Currently, the staff available to provide user assistance is composed of:\n" \
                     "{shopkeepers}\n" \
                     "<i>Click / Tap one of their names to contact them in a Telegram chat.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ The product has been successfully added/modified!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ The product has been successfully deleted!"

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
success_order_completed = "✅ You marked the order #{order_id} as completed"

# Success: order was refunded successfully
success_order_refunded = "✴️ Order #{order_id} has been successfully refunded."

successfull_payment = "Оплата совершена, ожидайте курьера"

# Success: transaction was created successfully
success_transaction_created = "✅ The transaction was created successfully!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ This bot only works in private chats."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ The conversation with the bot is interrupted.\n" \
                           "To restart it, send the /start command to the bot."

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
error_duplicate_name = "️⚠️ A product with this name already exists"

# Error: not enough credit to order
error_not_enough_credit = "⚠️ You do not have enough credit to place the order"

# Error: order has already been cleared
error_order_already_cleared = "⚠️  This order has already been processed."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  You have not placed orders yet, so there is nothing to display."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  The selected user does not exist"

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh no! An <b>error</b> interrupted this conversation\n" \
                               "The error was reported to the developer of greed so that he can fix it.\n" \
                               "To restart the conversation, send the /start command."
