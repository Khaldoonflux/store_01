import json
import os
from datetime import datetime, timedelta
import customtkinter as ctk

# إعدادات المظهر العام
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_FILE = "masraf_txns.json"


class MasrafApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("مصروف")
        self.geometry("430x750")
        self.resizable(False, False)

        # المتغيرات الأساسية
        self.is_dark = True
        self.user_email = ""
        self.records = []
        self.current_type = "Expense"  # الافتراضي مصروف

        self.load_local_data()

        # حاوية الشاشات الرئيسية
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        # التحقق من تسجيل دخول مسبق
        if self.user_email:
            self.show_main_screen()
        else:
            self.show_login_screen()

    # ══════════════════════════════
    # إدارة البيانات (JSON)
    # ══════════════════════════════
    def load_local_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.records = data.get("records", [])
                    self.user_email = data.get("user_email", "")
                    self.is_dark = data.get("is_dark", True)
                    mode = "dark" if self.is_dark else "light"
                    ctk.set_appearance_mode(mode)
            except:
                pass

    def save_local_data(self):
        data = {
            "records": self.records,
            "user_email": self.user_email,
            "is_dark": self.is_dark,
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # ══════════════════════════════
    # شاشة تسجيل الدخول
    # ══════════════════════════════
    def show_login_screen(self):
        self.clear_container()

        # الإطار الرئيسي للشاشة
        login_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        login_frame.pack(fill="both", expand=True, padx=20, pady=40)

        # الشعار (Badge)
        badge = ctk.CTkLabel(
            login_frame,
            text="م",
            font=("Almarai", 36, "bold"),
            text_color="#d4af37",
            fg_color="#0f0f0f" if self.is_dark else "#ffffff",
            width=80,
            height=80,
            corner_radius=26,
        )
        badge.pack(pady=(20, 10))

        # العنوان
        title = ctk.CTkLabel(
            login_frame, text="مصروف", font=("Almarai", 32, "bold")
        )
        title.pack(pady=5)

        # الوصف الإرشادي
        sub_title = ctk.CTkLabel(
            login_frame,
            text="سجّل مصاريفك ودخلك بسرعة،\nوبياناتك محفوظة محلياً وفي حسابك",
            font=("Almarai", 14),
            text_color="gray",
        )
        sub_title.pack(pady=10)

        # الميزات الإرشادية
        features = [
            ("تتبع المصاريف والدخل يومياً وأسبوعياً وشهرياً", "#ff9f43"),
            ("تقارير فورية بالرصيد الصافي للمحافظة على ميزانيتك", "#2ecc71"),
        ]
        for text, color in features:
            f_box = ctk.CTkFrame(
                login_frame,
                fg_color="#0f0f0f" if self.is_dark else "#e0e0e8",
                corner_radius=14,
            )
            f_box.pack(fill="x", pady=6, ipady=8)
            dot = ctk.CTkLabel(
                f_box,
                text="•",
                font=("Arial", 24),
                text_color=color,
                width=20,
            )
            dot.pack(side="right", padx=10)
            lbl = ctk.CTkLabel(
                f_box,
                text=text,
                font=("Almarai", 12),
                justify="right",
                anchor="e",
            )
            lbl.pack(side="right", fill="x", expand=True, padx=5)

        # زر الدخول بـ Google (محاكاة تجريبية مدمجة)
        login_btn = ctk.CTkButton(
            login_frame,
            text="تسجيل الدخول التجريبي عبر Google",
            font=("Almarai", 15, "bold"),
            fg_color="#ffffff",
            text_color="#1a1a2e",
            hover_color="#f0f0f5",
            height=50,
            corner_radius=18,
            command=self.handle_login,
        )
        login_btn.pack(side="bottom", fill="x", pady=20)

    def handle_login(self):
        self.user_email = "demo@example.com"
        self.save_local_data()
        self.show_main_screen()

    # ══════════════════════════════
    # الشاشة الرئيسية لإدخال البيانات
    # ══════════════════════════════
    def show_main_screen(self):
        self.clear_container()

        # شريط علوي (Topbar)
        topbar = ctk.CTkFrame(self.container, fg_color="transparent")
        topbar.pack(fill="x", padx=15, pady=10)

        mode_text = "فاتح" if self.is_dark else "داكن"
        self.mode_btn = ctk.CTkButton(
            topbar,
            text=mode_text,
            width=70,
            height=32,
            corner_radius=999,
            command=self.toggle_mode,
        )
        self.mode_btn.pack(side="left")

        user_name = self.user_email.split("@")[0]
        logout_btn = ctk.CTkButton(
            topbar,
            text=f"خروج ({user_name})",
            width=90,
            height=32,
            corner_radius=999,
            fg_color="#c0392b",
            hover_color="#96281b",
            command=self.sign_out,
        )
        logout_btn.pack(side="right")

        # نموذج المدخلات الرقمية
        form_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # لوحة اختيار النوع (مصروف / إيراد)
        self.type_btn = ctk.CTkButton(
            form_frame,
            text="مصروف",
            font=("Almarai", 22, "bold"),
            fg_color="#1a0a00",
            text_color="#ff9f43",
            height=80,
            corner_radius=18,
            command=self.toggle_transaction_type,
        )
        self.type_btn.pack(fill="x", pady=10)

        # حقل المبلغ
        self.amount_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="0",
            font=("Almarai", 36),
            justify="center",
            height=70,
            corner_radius=18,
        )
        self.amount_entry.pack(fill="x", pady=10)
        self.amount_entry.bind("<KeyRelease>", self.format_amount_input)

        # حقل التفاصيل/الوصف
        self.desc_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="التفاصيل أو البيان",
            font=("Almarai", 16),
            justify="center",
            height=50,
            corner_radius=18,
        )
        self.desc_entry.pack(fill="x", pady=10)

        # زر الحفظ
        self.save_btn = ctk.CTkButton(
            form_frame,
            text="حفظ العملية",
            font=("Almarai", 18, "bold"),
            fg_color="#c0392b",
            hover_color="#96281b",
            height=60,
            corner_radius=18,
            command=self.save_record,
        )
        self.save_btn.pack(fill="x", pady=20)

        # أزرار التقارير الفورية السفلية
        report_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        report_frame.pack(fill="x", side="bottom", pady=10)

        periods = [("monthly", "شهري"), ("weekly", "أسبوعي"), ("daily", "يومي")]
        for period, label in periods:
            btn = ctk.CTkButton(
                report_frame,
                text=label,
                font=("Almarai", 14, "bold"),
                corner_radius=12,
                command=lambda p=period: self.open_report(p),
            )
            btn.pack(side="left", expand=True, padx=5, fill="x")

    # ══════════════════════════════
    # منطق العمليات والواجهات المعالجة
    # ══════════════════════════════
    def toggle_transaction_type(self):
        if self.current_type == "Expense":
            self.current_type = "Income"
            self.type_btn.configure(
                text="إيراد", fg_color="#001a0a", text_color="#2ecc71"
            )
        else:
            self.current_type = "Expense"
            self.type_btn.configure(
                text="مصروف", fg_color="#1a0a00", text_color="#ff9f43"
            )

    def format_amount_input(self, event):
        # ميزة إضافة الفواصل آلياً أثناء الكتابة كما بالـ JS
        raw = self.amount_entry.get().replace(",", "")
        if raw.isdigit():
            formatted = "{:,}".format(int(raw))
            self.amount_entry.delete(0, "end")
            self.amount_entry.insert(0, formatted)

    def save_record(self):
        raw_amt = self.amount_entry.get().replace(",", "")
        try:
            amount = float(raw_amt)
        except ValueError:
            return  # تجاهل إذا لم يكن رقماً صالباً

        new_rec = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "type": self.current_type,
            "amount": amount,
            "description": self.desc_entry.get().strip(),
            "timestamp": datetime.now().isoformat(),
        }
        self.records.append(new_rec)
        self.save_local_data()

        # إفراغ الخانات وتأكيد الحفظ بصرياً
        self.amount_entry.delete(0, "end")
        self.desc_entry.delete(0, "end")

        self.save_btn.configure(
            text="✓ تم الحفظ بنجاح", fg_color="#27ae60", hover_color="#1e8449"
        )
        self.after(2000, self.reset_save_button)

    def reset_save_button(self):
        self.save_btn.configure(
            text="حفظ العملية", fg_color="#c0392b", hover_color="#96281b"
        )

    # ══════════════════════════════
    # معالجة وعرض التقارير المالية
    # ══════════════════════════════
    def open_report(self, period):
        today = datetime.now().date()
        income_sum = 0
        expense_sum = 0

        for r in self.records:
            try:
                r_date = datetime.strptime(r["date"], "%Y-%m-%d").date()
            except:
                continue

            is_match = False
            if period == "daily" and r["date"] == today.strftime("%Y-%m-%d"):
                is_match = True
            elif period == "weekly":
                start_week = today - timedelta(days=today.weekday() + 1)
                end_week = start_week + timedelta(days=6)
                if start_week <= r_date <= end_week:
                    is_match = True
            elif (
                period == "monthly"
                and r_date.month == today.month
                and r_date.year == today.year
            ):
                is_match = True

            if is_match:
                if r["type"] == "Income":
                    income_sum += r["amount"]
                else:
                    expense_sum += r["amount"]

        net_val = income_sum - expense_sum

        # إنشاء نافذة منبثقة مستقلة لعرض التقرير البصري للعملة
        popup = ctk.CTkToplevel(self)
        popup.title("التقرير المالي")
        popup.geometry("340x300")
        popup.resizable(False, False)
        popup.transient(self)
        popup.grab_set()

        title_lbl = ctk.CTkLabel(
            popup,
            text=f"التقرير الـ { 'الشهري' if period=='monthly' else 'الأسبوعي' if period=='weekly' else 'اليومي' }",
            font=("Almarai", 16, "bold"),
        )
        title_lbl.pack(pady=15)

        inc_lbl = ctk.CTkLabel(
            popup,
            text=f"إجمالي الدخل: {income_sum:,.2f}",
            font=("Almarai", 14),
            text_color="#2ecc71",
        )
        inc_lbl.pack(pady=5)

        exp_lbl = ctk.CTkLabel(
            popup,
            text=f"إجمالي المصاريف: {expense_sum:,.2f}",
            font=("Almarai", 14),
            text_color="#ff9f43",
        )
        exp_lbl.pack(pady=5)

        net_color = (
            "#2ecc71"
            if net_val > 0
            else "#ff9f43"
            if net_val < 0
            else "gray"
        )
        net_lbl = ctk.CTkLabel(
            popup,
            text=f"الصافي: {net_val:,.2f}",
            font=("Almarai", 18, "bold"),
            text_color=net_color,
        )
        net_lbl.pack(pady=20)

    # ══════════════════════════════
    # التحكم العام بالتطبيق والمظهر
    # ══════════════════════════════
    def toggle_mode(self):
        self.is_dark = not self.is_dark
        mode = "dark" if self.is_dark else "light"
        ctk.set_appearance_mode(mode)
        self.mode_btn.configure(text="فاتح" if self.is_dark else "داكن")
        self.save_local_data()
        # تحديث فوري لواجهة المستخدم الحالية
        self.show_main_screen()

    def sign_out(self):
        self.user_email = ""
        self.save_local_data()
        self.show_login_screen()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = MasrafApp()
    app.mainloop()
