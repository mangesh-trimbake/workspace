import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import os

class ProductSearchAllQuery(CommonBaseHandler):
    

    def post(self):
        self.set_headers()
        value = {}

        value1 = self.get_argument("product_name", default="", strip=False).replace("'", "___")
        if value1 != "":
            value["product_name"] = value1     

        sql = "SELECT a.*, u.image FROM product a, user u WHERE "
        for ele in value:
            temp = value[ele]
            sql += ele + " LIKE '%" + temp + "%' "

                   
        #print sql
        data = self.get_this_data(sql)
        #print data
        response_data = json.dumps({
            'success': {
                'code': success_obj.success_code_created,
                'message': success_obj.success_message,
                'data': data,
                'max_count': max_count
            }
        },
            default=self.date_handler,
            indent=4)
        
        self.write(response_data)
        self.finish()

class CommonBaseHandler(tornado.web.RequestHandler, email_html):
    @property
    def db(self):
        return self.application.db

    # def __init__(self):
    #     self.Time_limit_for_forgot_password_link = 1800  # in seconds

    def set_headers(self):
        self.set_header('Content-Type', 'application/json')

        self.set_header("Access-Control-Allow-Origin", "http://localhost:8000")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("X-Forwarded-Proto", "https")
        self.set_header("Front-End-Https", "on")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        
        
        
    def get_this_data(self, sql):
        print("inside get_this_data sql ---",sql)
        cursor_this_data = self.db.cursor()
        cursor_this_data.execute(sql)
        user_desc = cursor_this_data.description
        column_names = [col[0] for col in user_desc]
        this_data = cursor_this_data.fetchall()
        data = [dict(itertools.izip(column_names, row))
                for row in this_data]
        cursor_this_data.close()
        data = self.decode_data(data)
        print(data)
        if data:
            return data
        else:
            return None

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

            (r"/product/search_query", ProductSearchAllQuery),

        ]

        settings = dict(
            # template_path=os.path.join(os.path.dirname(__file__), "ab_html_files"),
            cookie_secret="46osdETzKXasdQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        )

        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = MySQLdb.connect(
            "localhost", "root", "root", "product", charset='utf8', use_unicode=True)





if __name__ == "__main__":
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.bind(8080)
    print "Server running on port 8080"
    server.start(0)  # Forks multiple sub-processes
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()
    



