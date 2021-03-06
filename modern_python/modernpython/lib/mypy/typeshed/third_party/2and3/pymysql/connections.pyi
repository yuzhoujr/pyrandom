from typing import Any, Optional, Type
from .charset import MBLENGTH as MBLENGTH, charset_by_name as charset_by_name, charset_by_id as charset_by_id
from .cursors import Cursor as Cursor
from .constants import FIELD_TYPE as FIELD_TYPE, FLAG as FLAG
from .constants import SERVER_STATUS as SERVER_STATUS
from .constants import CLIENT as CLIENT
from .constants import COMMAND as COMMAND
from .util import join_bytes as join_bytes, byte2int as byte2int, int2byte as int2byte
from .converters import escape_item as escape_item, encoders as encoders, decoders as decoders
from .err import raise_mysql_exception as raise_mysql_exception, Warning as Warning, Error as Error, InterfaceError as InterfaceError, DataError as DataError, DatabaseError as DatabaseError, OperationalError as OperationalError, IntegrityError as IntegrityError, InternalError as InternalError, NotSupportedError as NotSupportedError, ProgrammingError as ProgrammingError

sha_new = ...  # type: Any
SSL_ENABLED = ...  # type: Any
DEFAULT_USER = ...  # type: Any
DEBUG = ...  # type: Any
NULL_COLUMN = ...  # type: Any
UNSIGNED_CHAR_COLUMN = ...  # type: Any
UNSIGNED_SHORT_COLUMN = ...  # type: Any
UNSIGNED_INT24_COLUMN = ...  # type: Any
UNSIGNED_INT64_COLUMN = ...  # type: Any
UNSIGNED_CHAR_LENGTH = ...  # type: Any
UNSIGNED_SHORT_LENGTH = ...  # type: Any
UNSIGNED_INT24_LENGTH = ...  # type: Any
UNSIGNED_INT64_LENGTH = ...  # type: Any
DEFAULT_CHARSET = ...  # type: Any

def dump_packet(data): ...

SCRAMBLE_LENGTH_323 = ...  # type: Any

class RandStruct_323:
    max_value = ...  # type: Any
    seed1 = ...  # type: Any
    seed2 = ...  # type: Any
    def __init__(self, seed1, seed2): ...
    def my_rnd(self): ...

def pack_int24(n): ...
def unpack_uint16(n): ...
def unpack_int24(n): ...
def unpack_int32(n): ...
def unpack_int64(n): ...
def defaulterrorhandler(connection, cursor, errorclass, errorvalue): ...

class MysqlPacket:
    connection = ...  # type: Any
    def __init__(self, connection): ...
    def packet_number(self): ...
    def get_all_data(self): ...
    def read(self, size): ...
    def read_all(self): ...
    def advance(self, length): ...
    def rewind(self, position=0): ...
    def peek(self, size): ...
    def get_bytes(self, position, length=1): ...
    def read_length_coded_binary(self): ...
    def read_length_coded_string(self): ...
    def is_ok_packet(self): ...
    def is_eof_packet(self): ...
    def is_resultset_packet(self): ...
    def is_error_packet(self): ...
    def check_error(self): ...
    def dump(self): ...

class FieldDescriptorPacket(MysqlPacket):
    def __init__(self, *args): ...
    def description(self): ...
    def get_column_length(self): ...

class Connection:
    errorhandler = ...  # type: Any
    ssl = ...  # type: Any
    host = ...  # type: Any
    port = ...  # type: Any
    user = ...  # type: Any
    password = ...  # type: Any
    db = ...  # type: Any
    unix_socket = ...  # type: Any
    charset = ...  # type: Any
    use_unicode = ...  # type: Any
    client_flag = ...  # type: Any
    cursorclass = ...  # type: Any
    connect_timeout = ...  # type: Any
    messages = ...  # type: Any
    encoders = ...  # type: Any
    decoders = ...  # type: Any
    host_info = ...  # type: Any
    def __init__(self, host='', user=None, passwd='', db=None, port=3306, unix_socket=None, charset='', sql_mode=None, read_default_file=None, conv=..., use_unicode=None, client_flag=0, cursorclass=..., init_command=None, connect_timeout=None, ssl=None, read_default_group=None, compress=None, named_pipe=None): ...
    socket = ...  # type: Any
    rfile = ...  # type: Any
    wfile = ...  # type: Any
    def close(self): ...
    def autocommit(self, value): ...
    def commit(self): ...
    def begin(self) -> None: ...
    def rollback(self): ...
    def escape(self, obj): ...
    def literal(self, obj): ...
    def cursor(self, cursor: Optional[Type[Cursor]] = ...): ...
    def __enter__(self): ...
    def __exit__(self, exc, value, traceback): ...
    def query(self, sql): ...
    def next_result(self, unbuffered: bool = ...): ...
    def affected_rows(self): ...
    def kill(self, thread_id): ...
    def ping(self, reconnect: bool = ...): ...
    def set_charset(self, charset): ...
    def read_packet(self, packet_type=...): ...
    def insert_id(self): ...
    def thread_id(self): ...
    def character_set_name(self): ...
    def get_host_info(self): ...
    def get_proto_info(self): ...
    def get_server_info(self): ...
    def show_warnings(self): ...
    Warning = ...  # type: Any
    Error = ...  # type: Any
    InterfaceError = ...  # type: Any
    DatabaseError = ...  # type: Any
    DataError = ...  # type: Any
    OperationalError = ...  # type: Any
    IntegrityError = ...  # type: Any
    InternalError = ...  # type: Any
    ProgrammingError = ...  # type: Any
    NotSupportedError = ...  # type: Any

class MySQLResult:
    connection = ...  # type: Any
    affected_rows = ...  # type: Any
    insert_id = ...  # type: Any
    server_status = ...  # type: Any
    warning_count = ...  # type: Any
    message = ...  # type: Any
    field_count = ...  # type: Any
    description = ...  # type: Any
    rows = ...  # type: Any
    has_next = ...  # type: Any
    def __init__(self, connection): ...
    first_packet = ...  # type: Any
    def read(self): ...
