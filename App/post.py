def postresult(smiles,zinc,purchase,mwt,logp):
    x = '''
            </div>
                <a href="#smiles-table">
                    <div class="scroll-down">
                        <span>
                                <i class="fa fa-angle-down fa-2x"></i>
                        </span>
                    </div>
                    </a>
                    </div>
            </section>
            <section id="smiles-table" class="pfblock pfblock-gray">
                <div class="container">
                    <div class="row">
                    <div class="col-sm-4 border" id="jsmol" >
                        <script type="text/javascript">
                          jmolApplet0 = Jmol.getApplet("jmolApplet0", Info);
                          Jmol.script(jmolApplet0,"background [245,245,245]; load ${}; spin on")
                        </script>
                    </div>
                    <div class="col-sm-8 border">
                        <div class="table-responsive">
                        <h1>Here is your chemical:</h1>
                        <h3>smiles:<br><h4>{}</h4></h3>
                        <h3>zinc id:<br><h4>{}</h4></h3>
                        <h3>This chemical is :<br><h4>{}</h4></h3
                        </div>
                    </div>
                </div>
                <div class="col-sm-4 border">
                <h3>MWT {}</h3>
                <h3>LOGP {}</h3>
               </div>
            </section>
                <div class="scroll-up">
                    <a href="#home"><i class="fa fa-angle-up"></i></a>
                 </div>
        '''\
            .format(smiles,smiles,zinc,purchase,mwt,logp)
    return x
