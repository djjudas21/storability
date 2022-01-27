# Storability

Storability is a very simple storage availability tester.

The pod runs in an infinite loop which does the following:

* Get the current timestamp
* Save the current timestamp into a file on the PV to be tested
* Sleep for 1 second
* Read the timestamp back and make sure it matches what was written
* Warn you if they were different
* Repeat forever

This is ideal to set running before testing storage failover etc, to make sure that:

1. Storage remains available to user workloads
2. After storage has failed over, that the latest data is available on the replica

## Deploy

Choose **one** of the PVCs to deploy according to your region
and what storage class you want.

```sh
oc apply -f deploy/pvc-[region]-[storageclass].yaml
```

Then deploy the Storability pod

```sh
oc apply -f deploy/pod.yaml
```

Watch the output

```sh
oc logs -f storability
```

Don't forget to clean up when you're done, otherwise this will run forever!

```sh
oc delete pod storability
oc delete pvc storability
```

## Edit

Git repo: https://github.com/djjudas21/storability
Image registry: https://reg.1u1.it/harbor/projects/6/repositories/storability