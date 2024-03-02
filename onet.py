from langchain.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA





def onet_job_title_to_onet_code(resume_json , chat_llm ):

    new_dict = {}
    for i in resume_json['work']:
        key = i['organization']
        value = i['standardized_job_title']

        # make a new dictionary with the key and value
        new_dict[key] = value

    loader = CSVLoader(file_path=r"2019_Occupations.csv" ,encoding="utf-8", csv_args={
                    'delimiter': ','})

    data_onet = loader.load()

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    vectorstore = FAISS.from_documents(data_onet, embeddings)


    qa_chain = RetrievalQA.from_chain_type(llm=chat_llm,
                                      chain_type="stuff",
                                      retriever=vectorstore.as_retriever(),
                                      return_source_documents=True)



    query = f""" Map the give job title to the ONET code and title for give dictionary of job titles. 
    
    
    
    Dictionary : {new_dict} 
    
    """


    llm_response = qa_chain(query)

    return llm_response['result']
