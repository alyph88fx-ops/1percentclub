// 1 Percent Club: connection to the members database (Supabase).
// Both values are public by design: they sit in the browser, and the database's
// row-level security rules decide what each signed-in member may read or change.
// Never put the service_role / secret key here.
window.ONEPC = {
  supabaseUrl: '',
  supabaseKey: ''
};
