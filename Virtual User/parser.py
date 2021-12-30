import re

class Parser:

    def substitute_string(self, string, keywords,encode):
        original = string

        if encode == False:
            for word in keywords:
                string = re.sub('{}'.format(word), '{}'.format(word[2:-2]), string, flags = re.IGNORECASE)
        else:
            for word in keywords:
                string = re.sub(r'\b{}\b'.format(word), '#_{}_#'.format(word), string, flags = re.IGNORECASE)

        if encode == True:
            string = re.sub('<', '_l_', string)
            string = re.sub('>', '_g_', string)
            string = re.sub(';', '_sc_', string)
            string = re.sub('&', '_amp_', string)
        else:
            string = re.sub('_l_', '&lt;', string)
            string = re.sub('_g_', '&gt;', string)
            string = re.sub('_sc_', '&#59;', string)
            string = re.sub('_amp_', '&amp;', string)

        if (string != original):
            return (string, True)
        else:
            return (string, False)

    def encode(self, stringin):
        keywords = ["ADD", "ALTER", "ALL", "AND", "ANY", "AS", "BACKUP", "CASE", "CHECK", "CONSTRAINT", "CREATE", "DATABASE", "DELETE", "DROP", "EXEC", "HAVING", "IN", "INSERT", "INDEX", "LIKE", "SELECT", "SET", "TABLE", "TRUNCATE", "UPDATE" , "WHERE"]
        return self.substitute_string(stringin, keywords,True)

    def decode(self, stringin):
        keywords = ["#_ADD_#", "#_ALTER_#", "#_ALL_#", "#_AND_#", "#_ANY_#", "#_AS_#", "#_BACKUP_#", "#_CASE_#", "#_CHECK_#", "#_CONSTRAINT_#", "#_CREATE_#", "#_DATABASE_#", "#_DELETE_#", "#_DROP_#", "#_EXEC_#", "#_HAVING_#", "#_IN_#", "#_INSERT_#", "#_INDEX_#", "#_LIKE_#", "#_SELECT_#", "#_SET_#", "#_TABLE_#", "#_TRUNCATE_#", "#_UPDATE_#" , "#_WHERE_#"]
        return self.substitute_string(stringin, keywords,False)
