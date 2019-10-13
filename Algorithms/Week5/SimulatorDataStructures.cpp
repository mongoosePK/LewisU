// SimulatorDataStructures.cpp

// queuing_simulator.cpp
#include <iostream>
#include <stdlib.h>
#include <string>
#include <math.h>

using namespace std;
// --------------------- clock ----------------------
double wall_clock=0;
bool emergency_done = false;

// for status of nodes for management purposes
const int ev_available = 10;
const int ev_used = 11;
float ESIMUL_TIME = 10000;
int last_arrived_client = 100;

// for list types:
const int AV_list = 20;
const int EV_list = 21;
const int QU_list = 22;

// ------------------ events ------------------
// types of events:
const int E_SIMUL = 101; // end simulation
const int E_SVC = 102;   // end of service
const int ARRIVAL = 103; // arrival of client

struct ev_node
{
      float time;
      int type;
      ev_node *link;
      int stats_id; // client stats index
      int index;
};
// ------------------ client stats ------------------------
struct stats_client
{
      double in_system;
      double in_service;
      double out_system;
};


const int max_clients=20000;

struct clients
{
      stats_client CL[max_clients];
      float inter_arrival_time; // assumed Poisson Distribution
      int next_available_id;    // gives next available client record.
                                // current_client <= max_clients - 1
                                // current_client, total cnumber of clients
                                // in process or processed
};