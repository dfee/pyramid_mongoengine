import colander
import deform
import bcrypt

def prepare_password(value):
    '''Takes a password string and returns a bcrypt'd password'''
    return bcrypt.hashpw(value, bcrypt.gensalt())

class UserSchema(colander.MappingSchema):
    email = colander.SchemaNode(colander.String())
    username = colander.SchemaNode(colander.String())
    password = colander.SchemaNode(colander.String(),
                                   widget=deform.widget.PasswordWidget(),
                                   preparer=prepare_password)
    first_name = colander.SchemaNode(colander.String())
    last_name = colander.SchemaNode(colander.String())

class SigninSchema(colander.MappingSchema):
    username = colander.SchemaNode(colander.String())
    password = colander.SchemaNode(colander.String(),
                                   widget=deform.widget.PasswordWidget())

class ACLSchema(colander.MappingSchema):
    admin = colander.SchemaNode(colander.Boolean())
    manager = colander.SchemaNode(colander.Boolean())
