# asyncdb.py

import threading
from asyncdb_header import CDataBaseAsyncHelper, CScriptTriggerArgs, g_Serv

class CDataBaseAsyncHelperImpl(CDataBaseAsyncHelper):
    def onStart(self):
        super().on_start()
    
    def tick(self):
        if self.m_queriesTodo:
            current_pair = None
            with self.m_queryMutex:
                current_pair = self.m_queriesTodo.popleft()
            
            if current_pair:
                is_query, (s_function, s_query) = current_pair
                the_args = CScriptTriggerArgs()
                the_args.m_iN1 = is_query
                the_args.m_s1 = s_query
                
                if is_query:
                    the_args.m_iN2 = g_Serv._hDb.query(s_query, the_args.m_VarsLocal)
                else:
                    the_args.m_iN2 = g_Serv._hDb.exec(s_query)
                
                g_Serv._hDb.addQueryResult(s_function, the_args)

g_asyncHdb = CDataBaseAsyncHelperImpl()

# Example usage
if __name__ == "__main__":
    g_asyncHdb.start()

    g_asyncHdb.add_query(True, "some_function", "SELECT * FROM some_table")
    g_asyncHdb.add_query(False, "some_function", "UPDATE some_table SET column=value")

    # Ensure to stop the thread properly
    g_asyncHdb.wait_for_close()
    g_asyncHdb.join()
