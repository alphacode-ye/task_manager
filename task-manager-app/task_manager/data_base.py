# data_base.py
import sqlite3
import json
from task_manager.user import Encrypt


class Data:
    def __init__(self, user_name, password=None, log_phone=None):
        self.user = user_name
        self.password = password
        self.log_phone = log_phone
        self.file_path = r"data/data.db"
        self.encrypt = Encrypt()

    def create_connection(
        self,
    ):  # انشاء اتصال بين الكود وقاعدة البيانات وانشائها ان لم تكن موجودة
        try:
            conn = sqlite3.connect(f"{self.file_path}")
            return conn

        except Exception as e:
            print("Error while connecting:", e)
            return None

    def creat_Table(self):  # انشاء الجداول الخاصة بقاعدة البيانات ان لم تكن موجودة
        con = self.create_connection()
        try:
            cursor = con.cursor()
            cursor.execute(
                "PRAGMA foreign_keys = ON;"
            )  # تفعيل خاصية العلاقات في قاعدة البيانات
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                log_phone_use TEXT NOT NULL CHECK (log_phone_use GLOB '[0-2][0-9]:[0-5][0-9]')
                )"""
            )  # انشاء جدول المستخدمين باسم المستخدم والرمز ومدة الاستخدام للجهاز
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                user_ID INTEGER NOT NULL,
                description TEXT NOT NULL ,
                deadline TEXT NOT NULL CHECK (deadline GLOB '[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]'),
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                UNIQUE (user_ID, description)
                FOREIGN KEY (user_ID) REFERENCES users (id) ON DELETE CASCADE
                )"""
            )  # انشاء كلاس المهمات بجميع خصائصة وانشاء علاقة بين ايدي اليوزر والمهمة
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS subtasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                task_ID INTEGER NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (task_ID) REFERENCES tasks (id) ON DELETE CASCADE
                )"""
            )  # انشاء كلاس المهمات الفرعية وربط كل مهمة فرعيه بمهمتها الرئيسيه
            con.commit()
        except BaseException as e:
            print(f"Error: {e}")
            pass
        finally:
            con.close()

    def insert_user_data(
        self, user_name, password, log_phone
    ):  # دالة تعبئة الحقول في جدول المستخدمين
        con = self.create_connection()
        try:
            cursor = con.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (user_name,))
            user_exists = cursor.fetchone()[0] > 0
            if user_exists:
                pass
            else:
                cursor.execute(
                    """
                INSERT INTO users (username, password, log_phone_use) VALUES (?, ?, ?)
                """,
                    (user_name, password, log_phone),
                )
                con.commit()
        except BaseException as e:
            print(f"Error: {e}")
            pass
        finally:
            con.close()

    def insert_task_data(
        self, task, description, deadline, priority, status, username
    ):  # دالة تعبئة الحقول في جدول المهمات
        con = self.create_connection()
        try:
            cursor = con.cursor()
            user_ID = self.get_id(
                username, "users", "username"
            )  # جلب ايدي المسخدم لربطة بالمهمة الخاصة به
            cursor.execute(
                "SELECT COUNT(*) FROM tasks WHERE user_id = ? AND description = ?",
                (user_ID, description),
            )
            result = cursor.fetchone()

            if result[0] == 0:
                cursor.execute(
                    """
                INSERT INTO tasks (task, user_ID, description ,deadline ,priority ,status) VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (task, user_ID, description, deadline, priority, status),
                )
                con.commit()
        except BaseException as e:
            print(f"Error task: {e}")
            pass
        finally:
            con.close()

    def get_id(self, name, tabel, colom):  # جلب ايدي من اي جدول والعامود حسب الاسم
        conn = self.create_connection()
        cursor = conn.cursor()
        query = f"SELECT id FROM {tabel} WHERE {colom} = ?"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def get_task_id(
        self, task, user_name
    ):  # البحث عن اي مهمه حسب اسم المهمة واسم المستخدم
        con = self.create_connection()
        cursor = con.cursor()
        user_ID = self.get_id(
            user_name, "users", "username"
        )  # جلب ايدي المستخدم لكي يتم البحث عن المهام
        cursor.execute(f"SELECT id,task,user_ID FROM tasks WHERE user_ID = {user_ID}")
        result = cursor.fetchall()
        for (
            i,
            e,
            k,
        ) in result:  # هاذي سيتم تعديلها ولاكنها تستخدم لجلب الايدي فقط للمهمه
            if k == user_ID:
                if e == task:
                    return i
            else:
                pass

    def insert_subtask_data(
        self, subtask, status, task
    ):  # ادخال البيانات في جدول المهام الفرعية
        con = self.create_connection()
        try:
            cursor = con.cursor()
            task_ID = self.get_task_id(
                task, self.user
            )  # جلب ايدي المهمه التي سيضاف لها مهمة فرعية
            cursor.execute(
                "SELECT COUNT(*) FROM subtasks WHERE task_id = ? AND task = ?",
                (task_ID, subtask),
            )
            result = cursor.fetchone()
            if result[0] == 0:
                cursor.execute(
                    """
                INSERT INTO subtasks (task,status,task_ID) VALUES (?, ?, ?)
                """,
                    (subtask, status, task_ID),
                )
                con.commit()
        except BaseException as e:
            print(f"Error subtask: {e}")
            pass
        finally:
            con.close()

    # هاذه الدالة تقوم بحذف لبيانات من الجداول عبر تحديد الجدول ثم تحديد عامودين من الجدول وادخال قيمتين للجدول
    def delete_data(
        self,
        table_name,
        condition1_column,
        condition1_value,
        condition2_column,
        condition2_value,
    ):
        conn = self.create_connection()
        try:
            cursor = conn.cursor()
            query = f"DELETE FROM {table_name} WHERE {condition1_column} = ? AND {condition2_column} = ?"
            cursor.execute(query, (condition1_value, condition2_value))
            conn.commit()
        except BaseException as e:
            print(f"Error: {e}")
            pass
        finally:
            conn.close()

    def from_js_to_data(
        self,
    ):  # تحويل البيانات من ملف البيانات الي قاعدة البيانات لتكون مرتبة
        try:
            with open("data/data.json", "r+") as file:
                key = self.encrypt.load_key()
                user_data = json.load(file)
                data = self.encrypt.decrypt_data(user_data,key)
                user_info = data.get(self.user, {})
                old_password = user_info.get("password", self.password)
                log_phone_usa = user_info.get("log_phone_usa", self.log_phone)
                self.insert_user_data(self.user, old_password, log_phone_usa)
                task_list = user_info.get("task_list", {})
                for (
                    task_name,
                    details,
                ) in (
                    task_list.items()
                ):  # استخراج البيانات من الملف ليتم تضمينها في قاعدة البيانات
                    task = task_name
                    Description = details["description"]
                    Deadline = details["deadline"]
                    Priority = details["priority"]
                    status = details["status"]
                    self.insert_task_data(
                        task, Description, Deadline, Priority, status, self.user
                    )  # اضافة بيانات المهمة لقاعدة البيانات
                    if details[
                        "subtask"
                    ]:  # اضافة بيانات المهام الفرعية لجدول المهام الفرعية
                        for sub in details["subtask"]:
                            subtask = list(sub.keys())
                            subtaskVL = list(sub.values())
                            self.insert_subtask_data(subtask[0], subtaskVL[0], task)

        except (json.JSONDecodeError, FileNotFoundError):
            with open("data\\data.json", "w") as file:
                return None
            pass

    def git_tasks(self, status=None):  # جلب كل المهمات االخاصة بمستخدم محدد
        conn = self.create_connection()
        try:
            cursor = conn.cursor()
            user = self.get_id(self.user, "users", "username")
            query = f"SELECT COUNT(*) FROM tasks WHERE user_ID = ? AND status = ?"
            cursor.execute(query, (user, status))
            result = cursor.fetchone()
            conn.commit()
            return result[0]
        except BaseException as e:
            print(f"Error: {e}")
            pass
        finally:
            conn.close()

    def export_to_json(self):#جلب البيانات من قاعدة البيانات وتحويلها (json)
        conn = self.create_connection()
        try:
            cursor = conn.cursor()
            # جلب جميع المستخدمين
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            user_columns = [column[0] for column in cursor.description]

            # جلب جميع المهام
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            task_columns = [column[0] for column in cursor.description]

            # جلب جميع المهام الفرعية
            cursor.execute("SELECT * FROM subtasks")
            subtasks = cursor.fetchall()
            subtask_columns = [column[0] for column in cursor.description]

            # بناء الهيكل المطلوب
            data = {}
            for user in users:
                user_data = dict(zip(user_columns, user))
                user_id = user_data.pop("id")  # استخراج معرف المستخدم
                data[user_data["username"]] = {
                    "name": user_data["username"],
                    "password": user_data.get("password", ""),
                    "log_phone_usa": user_data.get("log_phone_usa", ""),
                    "task_list": {}
                }
                # print(tasks)

                # جلب المهام الخاصة بالمستخدم
                user_tasks = [task for task in tasks if task[2] == user_id]
                for task in user_tasks:
                    task_data = dict(zip(task_columns, task))
                    task_id = task_data.pop("id")  # استخراج معرف المهمة
                    task_name = task_data.pop("task")  # اسم المهمة
                    data[user_data["username"]]["task_list"][task_name] = {
                        "task": task_name,
                        "description": task_data.get("description", ""),
                        "deadline": task_data.get("deadline", ""),
                        "priority": task_data.get("priority", ""),
                        "status": task_data.get("status", ""),
                        "subtask": []
                    }

                    # جلب المهام الفرعية الخاصة بالمهمة
                    task_subtasks = [subtask for subtask in subtasks if subtask[2] == task_id]
                    for subtask in task_subtasks:
                        subtask_data = dict(zip(subtask_columns, subtask))
                        subtask_name = subtask_data.get("task", "")
                        subtask_status = subtask_data.get("status", "")
                        data[user_data["username"]]["task_list"][task_name]["subtask"].append({
                            subtask_name: subtask_status
                        })
            key = self.encrypt.load_key()
            dataE = self.encrypt.encrypt_data(data,key)
            # كتابة البيانات إلى ملف JSON
            with open("data/data.json", "w", encoding="utf-8") as json_file:
                json.dump(dataE, json_file, ensure_ascii=False, indent=4)
        except BaseException as e:
            # print(f"Error: {e}")
            pass
        finally:
            conn.close()
    

if __name__ == "__main__":
    f = Data("yswef", "123", "12:12")
    f.export_to_json()