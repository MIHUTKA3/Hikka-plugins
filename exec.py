# meta developer: @MIHUTKA3

from hikkatl.types import Message
from .. import loader, utils
from io import StringIO
import sys

@loader.tds
class Exec(loader.Module):
    """Execute your python command"""
    strings = {
        "name": "Exec",
        "command": "Command:",
        "out": "Out:",
        "error": "An error occurred while executing the code:",
        "err": "Error:"
    }
    strings_ru = {
        "exec": "Exec",
        "command": "Команда:",
        "out": "Вывод:",
        "error": "Произошла ошибка при выполнении кода:",
        "err": "Ошибка:",
        "_cls_doc": "Выполните свою python команду"
    }
    @loader.command(ru_doc="Выполнить команду")
    async def exec(self, message: Message):
        """Execute the command"""

        code = utils.get_args_raw(message)
        if code:
            try:
                output = sys.stdout = StringIO()
                exec(code)
                val = output.getvalue()
                if val.strip():
                    await utils.answer(message, f'<emoji document_id=5877565553761062314>💻</emoji> {self.strings("command")}\n'
                                                f'    {code}\n\n<emoji document_id=5328239124933515868>📤️</emoji> {self.strings("out")}\n'
                                                f'    {output.getvalue()}')
            except Exception as error:
                await utils.answer(message, f'<emoji document_id=5291810741337206919>❌️</emoji> {self.strings("error")}\n'
                                            f'    <emoji document_id=5877565553761062314>💻</emoji> ️{self.strings("command")}\n'
                                            f'        {code}\n\n'
                                            f'    <emoji document_id=5877477244938489129>⚠</emoji> {self.strings("err")}\n'
                                            f'        {error}')
        else:
            await utils.answer(message, f'<emoji document_id=5877565553761062314>💻</emoji> {self.strings("command")}\n'
                                        f'    \n\n<emoji document_id=5328239124933515868>📤️</emoji> {self.strings("out")}\nNone')